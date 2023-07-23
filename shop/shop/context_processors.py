from app_cart.cart import Cart
from app_main.models import AboutUs


def get_about_us(request):
    try:
        company = AboutUs.objects.last()
    except:
        company = None
    return locals()


def cart(request):
    cart = Cart(request)
    return locals()
