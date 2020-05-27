import csv
from django.shortcuts import render
from .models import Column, CsvFilename

#


def table_view(request):
    CSV_FILENAME = CsvFilename.objects.first().get_path()
    COLUMNS = Column.objects.all().values().order_by('ordinal_number')
    template = 'table.html'

    with open(CSV_FILENAME, 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        context = {
            'columns': COLUMNS,
            'table': table,
            'csv_file': CSV_FILENAME
        }
        result = render(request, template, context)
    return result
