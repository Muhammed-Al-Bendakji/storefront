from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product
from store.models import Order


# def hello(request):
# try:
#     product = Product.objects.get(pk=0)
# except ObjectDoesNotExist:
#     pass

# We can use filter instead of Try catch exception.
# quaryset = Product.objects.filter(unit_price__range=(20, 30))

# import Q objact ot usr or condition
# quaryset = Product.objects.filter(
#     Q(inventory__lt=20) | ~Q(unit_price__gt=10)).order_by('title')

# get last 5 orders with there customers and items inclouding product

# quaryset = Order.objects.select_related(
#     'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

# return render(request, 'hello.html', {'orders': (list(quaryset))})

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Mosh'})
