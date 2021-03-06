# Generated by Django 2.2.10 on 2020-05-16 15:54

from django.db import migrations


def data_migrate(apps, schema_editor):
    Student = apps.get_model('school', 'Student')
    for student in Student.objects.all():
        student.teacher_tmp.add(student.teacher_id)


class Migration(migrations.Migration):
    dependencies = [
        ('school', '0003_add_tmp_field'),
    ]

    operations = [
        migrations.RunPython(data_migrate)
    ]