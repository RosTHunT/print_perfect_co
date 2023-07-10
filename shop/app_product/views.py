from django.shortcuts import render
from django.views import View


# Create your views here.
class ProductView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'app_product/product.html', context=context)
