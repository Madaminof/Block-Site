# Generated by Django 5.0.6 on 2024-06-03 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_createuser_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createuser',
            name='likes',
        ),
    ]