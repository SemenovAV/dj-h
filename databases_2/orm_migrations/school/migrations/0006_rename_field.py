# Generated by Django 2.2.10 on 2020-05-16 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_remove_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher_tmp',
            new_name='teacher',
        ),
    ]