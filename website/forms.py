from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control nexus-input',
            'placeholder': 'Email Address',
            'autocomplete': 'email',
        })
    )
    first_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control nexus-input',
            'placeholder': 'First Name',
            'autocomplete': 'given-name',
        })
    )
    last_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control nexus-input',
            'placeholder': 'Last Name',
            'autocomplete': 'family-name',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control nexus-input'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted small"><i class="bi bi-info-circle"></i> Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control nexus-input'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small nexus-help-list"><li>Can\'t be too similar to your personal information.</li><li>Must contain at least 8 characters.</li><li>Can\'t be a commonly used password.</li><li>Can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control nexus-input'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted small"><i class="bi bi-info-circle"></i> Enter the same password as before, for verification.</span>'


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        label='', required=True, max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control nexus-input',
            'placeholder': 'First Name',
        })
    )
    last_name = forms.CharField(
        label='', required=True, max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control nexus-input',
            'placeholder': 'Last Name',
        })
    )
    email = forms.EmailField(
        label='', required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control nexus-input',
            'placeholder': 'Email Address',
        })
    )
    phone_number = forms.CharField(
        label='', required=True, max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control nexus-input',
            'placeholder': 'Phone Number',
        })
    )
    address = forms.CharField(
        label='', required=True, max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control nexus-input',
            'placeholder': 'Address',
        })
    )
    city = forms.CharField(
        label='', required=True, max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control nexus-input',
            'placeholder': 'City',
        })
    )
    zipcode = forms.CharField(
        label='', required=True, max_length=6,
        widget=forms.TextInput(attrs={
            'class': 'form-control nexus-input',
            'placeholder': 'Zipcode',
        })
    )

    class Meta:
        model = Record
        exclude = ('user',)