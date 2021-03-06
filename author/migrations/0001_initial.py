# Generated by Django 3.2.8 on 2021-10-24 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=60)),
                ('displayName', models.CharField(max_length=120, null=True)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar')),
                ('bgImage', models.ImageField(blank=True, null=True, upload_to='background')),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('jobName', models.CharField(default='Author Job', max_length=20)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
