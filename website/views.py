from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Incorrect credentials. Please try again.')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Incorrect credentials. Please try again.')
            return redirect('home')
    else:
        return render(request, 'login.html')



def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You have successfully registered! Welcome!')
                    return redirect('home')
                else:
                    messages.error(request, 'Registration succeeded but auto-login failed. Please log in manually.')
                    return redirect('home')
            except IntegrityError:
                messages.error(request, 'That username is already taken. Please choose another.')
                return render(request, 'register.html', {'form': form})
            except Exception:
                messages.error(request, 'An error occurred during registration. Please try again.')
                return render(request, 'register.html', {'form': form})
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        try:
            customer_record = Record.objects.get(id=pk)
            return render(request, 'record.html', {'customer_record': customer_record})
        except Record.DoesNotExist:
            messages.error(request, 'Record not found.')
            return redirect('home')
    else:
        messages.error(request, 'You must be logged in to view records.')
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        try:
            delete_it = Record.objects.get(id=pk)
            delete_it.delete()
            messages.success(request, 'Record has been deleted successfully.')
        except Record.DoesNotExist:
            messages.error(request, 'Record not found.')
        return redirect('home')
    else:
        messages.error(request, 'You must be logged in to perform this action.')
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, 'Record has been added successfully!')
                    return redirect('home')
                except Exception:
                    messages.error(request, 'An error occurred while saving the record.')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to add records.')
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        try:
            current_record = Record.objects.get(id=pk)
        except Record.DoesNotExist:
            messages.error(request, 'Record not found.')
            return redirect('home')
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Record has been updated successfully!')
                return redirect('home')
            except Exception:
                messages.error(request, 'An error occurred while updating the record.')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to update records.')
        return redirect('home')


def about(request):
    return render(request, 'about.html')


def features(request):
    return render(request, 'features.html')


def contact(request):
    if request.method == 'POST':
        messages.success(request, 'Thank you for reaching out! We\'ll get back to you soon.')
        return redirect('contact')
    return render(request, 'contact.html')