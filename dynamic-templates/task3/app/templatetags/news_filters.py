from datetime import datetime

from django import template

register = template.Library()


def pluralRusVariant(x):
    if x % 10 == 1 and x % 100 != 11:
        return 0

    elif x % 10 in [2, 3, 4] and x % 100 not in [12, 13, 14]:
        return 1
    elif x % 10 == 0 or x % 10 in [5, 6, 7, 8, 9] or x % 100 in [11, 12, 13, 14]:
        return 2
    return 2


def showHours(hours):
    suffix = ["час", "часа", "часов"][pluralRusVariant(hours)]
    return f'{hours} {suffix}'


@register.filter()
def format_date(value):
    time = datetime.now() - datetime.utcfromtimestamp(value)
    min = time.seconds / 60
    if min < 10:
        return "только что"
    elif 10 < min < 1440:
        return f' {showHours(round(min / 60))} назад'
    elif 1440 < min:
        return datetime.strftime(datetime.now() - time, '%Y %B %d')


@register.filter()
def format_score(value, default=None):
    if not value:
        return default
    if value < -5:
        return "всё плохо"
    elif -4 < value < 6:
        return "нейтрально"
    elif value > 5:
        return "хорошо"


@register.filter()
def format_num_comments(value):
    if not value:
        return "Оставьте комментарий"
    if 0 < value < 50:
        return f'{value}'
    if value > 50:
        return '50+'


@register.filter()
def format_selftext(value, count=None):
    if count:
        text = value.split(' ')
        if len(text) > count * 2:
            start = text[:count:]
            end = text[len(text) - count * 2::]
            strings = ' '.join(start) + ' ... ' + ' '.join(end)
            return strings
        else:
            return value or ''
    else:
        return value or ''
