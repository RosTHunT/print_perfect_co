from django.urls import path
from . import views

app_name = 'app_cart'

urlpatterns = [
    path('', views.CartDetailsView.as_view(), name='cart_detail')
    # path('add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add_view'),
    # path('remove/<int:product_id>/', views.CartRemoveView.as_view(),  name='cart_remove_view'),
    # path('change-quantity-product/', views.ChangeQuantityProductInCartView.as_view(),  name='change_quantity_product_in_cart'),

]