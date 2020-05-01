from datetime import datetime

from app.views import file_list, file_content
from django.urls import path, register_converter


class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    def __init__(self):
        self.date_format = "%Y-%m-%d"

    def to_python(self, value):
        return datetime.strptime(value, self.date_format).date()

    def to_url(self, value):
        return value.strftime(self.date_format)


register_converter(DateConverter, 'datetime')

urlpatterns = [
    path('', file_list, name='file_list'),
    path('<datetime:date>/', file_list, name='file_list'),
    path('file/<name>', file_content, name='file_content'),
]
