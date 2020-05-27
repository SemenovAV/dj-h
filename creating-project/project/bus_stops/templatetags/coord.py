from django import template
from django.template.defaultfilters import floatformat

register = template.Library()


def coord(value):
    value = floatformat(value, arg=4)
    return str(value).replace(',', '.')


register.filter('coord', coord)
