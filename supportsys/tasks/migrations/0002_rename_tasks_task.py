# Generated by Django 4.2 on 2023-04-06 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mfaofficers', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]
