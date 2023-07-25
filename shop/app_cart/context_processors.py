from app_cart.cart import Cart
from app_main.models import AboutUs


def get_cart(request):
    cart = Cart(request)
    return locals()
