# Generated by Django 2.2.10 on 2020-05-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('width', models.PositiveSmallIntegerField()),
                ('ordinal_number', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CsvFilename',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FilePathField(match='.csv$', path='.')),
            ],
        ),
    ]
