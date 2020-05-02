from django import template

register = template.Library()


@register.filter('float_value')
def float_value(value: str) -> float:
    return float(value)
