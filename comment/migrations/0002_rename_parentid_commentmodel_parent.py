# Generated by Django 3.2.8 on 2021-10-25 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='parentId',
            new_name='parent',
        ),
    ]