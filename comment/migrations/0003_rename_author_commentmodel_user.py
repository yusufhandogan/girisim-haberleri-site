# Generated by Django 3.2.8 on 2021-10-25 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_rename_parentid_commentmodel_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='author',
            new_name='user',
        ),
    ]
