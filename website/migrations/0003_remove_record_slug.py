# Generated by Django 5.0.7 on 2024-09-17 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_record_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='slug',
        ),
    ]
