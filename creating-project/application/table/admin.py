from django.contrib import admin
from .models import CsvFilename, Column


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    pass


@admin.register(CsvFilename)
class CsvFilenameAdmin(admin.ModelAdmin):
    pass
