from django.db import models


class Column(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False)
    width = models.PositiveSmallIntegerField()
    ordinal_number = models.PositiveSmallIntegerField()


class CsvFilename(models.Model):
    path = models.FilePathField(
        path='/',
        match='^phones.csv$',
        recursive=False
    )
