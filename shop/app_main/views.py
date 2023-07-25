from django.shortcuts import render
from django.views import View

from app_product.models import Category, Product


class IndexView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(request, 'app_main/index.html', context=context)


class BlankView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'app_main/blank.html', context=context)


class CheckoutView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'app_main/checkout.html', context=context)


class StoreView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.filter(is_published=True)
        context = {
            'category': categories,
        }
        return render(request, 'app_main/store.html', context=context)