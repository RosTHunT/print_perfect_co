from app_cart.cart import Cart
from app_main.models import AboutUs


def get_about_us(request):
    try:
        company = AboutUs.objects.last()
    except:
        company = None
    return locals()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return locals()
