from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from app_product.models import Product


class Cart(object):
    def __init__(self, request):
        """ініціалізуємо корзину через сесію"""

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """Перебираємо товари в корзині і получаем товари з бази данних."""

        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Рахуємо кількість товарів в корзині"""

        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """Добавляєм товар в корзину або оновлюємо його кількість."""

        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """зберігаємо товар в корзині"""

        self.session.modified = True

    def remove(self, product):
        """видаляємо товар з корзини"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        """получаємо загальну вартість"""

        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def get_total_quantity(self):
        """получаємо загальну кількість"""

        return sum(item['quantity'] for item in self.cart.values())

    @property
    def json_products_range(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = {'id': product.pk}

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']

            item['price'] = str(item['price'])
            item['total_price'] = str(item['total_price'])

            yield item

    def get_json(self):
        response = {
            'products': [],
            'total_price': str(self.get_total_price()),
            'total_quantity': self.get_total_quantity()
        }

        for product_obj in self.json_products_range:
            product = get_object_or_404(Product, pk=product_obj['product']['id'])

            data = {
                'product': {
                    'id': product.pk,
                    'image': product.image.url if product.image else '#',
                },
                'name': product.name,
                'category': product.categories.name,
                'price': product_obj['price'],
                'total_price': product_obj['total_price'],
                'quantity': product_obj['quantity']
            }

            response['products'].append(data)

        return response

    def clear(self):
        """очищаємо сесію корзини"""

        del self.session[settings.CART_SESSION_ID]
        self.save()
