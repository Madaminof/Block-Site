# Generated by Django 5.0.6 on 2024-05-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_latestnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('tel', models.CharField(max_length=20)),
            ],
        ),
    ]
