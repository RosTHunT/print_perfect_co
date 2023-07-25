from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from app_cart.cart import Cart
from app_cart.forms import CartAddProductForm
from app_product.models import Product


class CartDetailsView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'app_cart/cart-deatils.html', context=context)


class CartAddView(View):
    def post(self, request, product_id, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=1,
                     # quantity=1 if cd['quantity'] in None else cd['quantity'],
                     update_quantity=cd['update'])

        redirect_url = self.request.META.get('HTTP_REFERER')
        if redirect_url:
            return HttpResponseRedirect(redirect_url)
        return redirect('app_main:index')


class CartRemoveView(View):
    def post(self, request, product_id, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)

        redirect_url = self.request.META.get('HTTP_REFERER')
        if redirect_url:
            return HttpResponseRedirect(redirect_url)
        return redirect('app_main:index')


class ChangeQuantityProductInCartView(View):
    def get(self, request, *args, **kwargs):
        pass