# Generated by Django 2.2.7 on 2019-11-26 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='action',
            new_name='done',
        ),
    ]
