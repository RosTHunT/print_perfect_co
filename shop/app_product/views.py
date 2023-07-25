from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from app_cart.cart import Cart
from app_product.models import Product


class ProductListView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(is_published=True)
        context = {
            'products': products
        }
        return render(request, 'app_product/product_list.html', context=context)


# Create your views here.
class ProductView(View):
    def get(self, request, product_id, **kwargs):
        product = get_object_or_404(Product, pk=product_id)
        context = {
            'product': product,
        }
        return render(request, 'app_product/product.html', context=context)


