import datetime
from csv import reader

from django.conf import settings
from django.shortcuts import render
from django.template.defaultfilters import date


def inflation_view(request):
    template_name = 'inflation.html'
    with open(settings.INFLATION_CSV, encoding='utf8') as f:
        r = reader(f, delimiter=';', )
        data = [val for val in r][1:]
    month = [date(datetime.date(2020, value, 1), 'F') for value in range(1, 13)]
    context = {
        'first_head': 'Год',
        'last_head': 'Всего',
        'month': month,
        'data': data

    }

    return render(request, template_name,
                  context)
