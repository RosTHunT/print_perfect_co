from django.urls import path

from . import views

app_name = 'app_product'

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='product_list'),
    path('<int:product_id>/', views.ProductView.as_view(), name='product'),

]
