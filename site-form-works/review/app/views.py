from django.shortcuts import render, get_object_or_404, redirect, reverse

from .forms import ReviewForm
from .models import Product, Review


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    session = request.session
    session.setdefault('review', [])
    context = {
        'product': product,
        'reviews': Review.objects.select_related('product').filter(product=product)
    }

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            Review.objects.create(**cleaned_data, product_id=pk)
            session['review'] = session['review'] + [pk]
        context['form'] = form
    else:
        context['form'] = ReviewForm
    context['is_review_exist'] = pk in session['review']

    return render(request, template, context)
