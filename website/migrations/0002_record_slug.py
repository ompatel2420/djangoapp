# Generated by Django 5.0.7 on 2024-09-17 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
