from csv import DictReader
from urllib.parse import urlencode
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='windows-1251') as f:
        paginator = Paginator([elem for elem in DictReader(f)], 8)
    current_page = request.GET.get('page', 1)
    strings = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if strings.has_previous():
        prev_page = f'?{urlencode({"page":strings.previous_page_number()})}'
    if strings.has_next():
        next_page = f'?{urlencode({"page":strings.next_page_number()})}'
    return render_to_response('index.html', context={
        'bus_stations': strings,
        'current_page': current_page,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
    })
