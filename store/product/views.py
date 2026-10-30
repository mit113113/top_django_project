from django.shortcuts import render

from .models import Product


def test(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'products/product_list.html', context)