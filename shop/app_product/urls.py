from django.urls import path

from . import views

app_name = 'app_product'

urlpatterns = [
    path('', views.ProductView.as_view(), name='product'),

]
