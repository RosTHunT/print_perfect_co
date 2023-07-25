from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва')
    is_published = models.BooleanField(default=False, verbose_name='Опублікувати Категорію')
    recommended = models.BooleanField(default=False, verbose_name='Рекомендувати Категорію')

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Категорію'
        verbose_name_plural = 'КатегоріЇ'

    def __str__(self):
        return f'Категорія: {self.title}'


class Product(models.Model):
    title = models.CharField(max_length=1024, blank=True, null=True)
    image = models.ImageField(upload_to='upload/products/images/%Y/%m/%d/', blank=True, null=True)
    description = models.TextField(max_length=5000, blank=True, null=True)

    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    price_last = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    recommended = models.BooleanField(default=False, verbose_name='Рекомендувати товар')

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')

    quantity = models.PositiveIntegerField()

    is_published = models.BooleanField(default=False)

    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def str_price(self):
        return f'₴ { self.price } грн'

    def str_price_without_sym(self):
        return f'{self.price} грн'

    # def delete(self, *args, **kwargs):
    #     if self.image and os.path.exists(self.image.path):
    #         os.remove(self.image.path)
    #
    #     if self.product_file:
    #         self.product_file.products_count -= 1
    #         self.product_file.save()
    #
    #     return super(Product, self).delete(*args, **kwargs)

    def __str__(self):
        return f' {self.title} | {self.category}'
