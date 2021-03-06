# Generated by Django 2.2.10 on 2020-05-27 10:05

from django.db import migrations

CSV_FILENAME = 'phones.csv'
COLUMNS = [
    {'name': 'id', 'width': 1},
    {'name': 'name', 'width': 3},
    {'name': 'price', 'width': 2},
    {'name': 'release_date', 'width': 2},
    {'name': 'lte_exists', 'width': 1},
]


def add_path(apps, schema_editor):
    file_path = apps.get_model('table', 'CsvFilename')
    file_path.objects.create(path=CSV_FILENAME)


def add_columns(apps, schema_editor):
    column = apps.get_model('table', 'Column')
    for i, elem in enumerate(COLUMNS):
        name = elem.get('name')
        width = elem.get('width')
        column.objects.create(ordinal_number=i, name=name, width=width)


class Migration(migrations.Migration):
    dependencies = [
        ('table', '0001_create_models'),
    ]

    operations = [
        migrations.RunPython(add_path),
        migrations.RunPython(add_columns)
    ]
