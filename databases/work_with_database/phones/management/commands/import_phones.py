import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            title = next(phone_reader)
            title.append('slug')
            for line in phone_reader:
                line[-1] = slugify(line[1])
                Phone.objects.create(**{key: value for key, value in zip(title, line)})


