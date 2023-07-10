from django.urls import path

from . import views

app_name = 'app_main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('blank/', views.BlankView.as_view(), name='blank'),
    # path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    # path('product/', views.ProductView.as_view(), name='product'),
    path('store/', views.StoreView.as_view(), name='store'),
]
