from collections import Counter
from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()


def index(request):
    param = request.GET.get('from-landing')
    if param:
        counter_click[param] += 1
    return render_to_response('index.html')


def landing(request):
    param = request.GET.get('ab-test-arg')
    variants = {
        'original': 'landing.html',
        'test': 'landing_alternate.html'
    }
    if param and param in variants:
        counter_show[param] += 1
    return render_to_response(variants.get(param) or '')


def stats(request):

    def conversion(target):
        click = counter_click.get(target)
        show = counter_show.get(target)
        return round(click / show if show else 0, 2)

    return render_to_response('stats.html', context={
        'test_conversion': conversion('test'),
        'original_conversion': conversion('original'),
    })
