from django.shortcuts import render

from .models import Phone


def show_catalog(request, name='name'):
    template = 'catalog.html'
    phones = Phone.objects.all().order_by(name)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
