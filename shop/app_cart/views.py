from django.shortcuts import render
from django.views import View

from app_cart.cart import Cart


class CartDetailsView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'app_cart/cart-deatils.html', context=context)


class CartAddView(View):
    def get(self, request, *args, **kwargs):
        pass


class CartRemoveView(View):
    def get(self, request, *args, **kwargs):
        pass


class ChangeQuantityProductInCartView(View):
    def get(self, request, *args, **kwargs):
        pass