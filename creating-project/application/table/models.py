from django.db import models


class Column(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False)
    width = models.PositiveSmallIntegerField()
    ordinal_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class CsvFilename(models.Model):
    path = models.FilePathField(
        path='.',
        match='.csv$',
        recursive=False
    )

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        return self.path
    def __str__(self):
        return self.path
