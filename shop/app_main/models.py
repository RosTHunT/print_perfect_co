from django.db import models


class AboutUs(models.Model):
    name = models.CharField(max_length=48, verbose_name='Імя')
    logo = models.ImageField(upload_to='logo/%Y/%m/%d', verbose_name='Лого', blank=True, null=True)

    address = models.CharField(max_length=256, blank=True, verbose_name='Адресса')
    email = models.EmailField(max_length=48,  blank=True, null=True, verbose_name='Електронна пошта')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон')

    short_description = models.TextField(max_length=512, verbose_name='Короткий опис')
    description = models.TextField(max_length=2048, verbose_name='Довгий опис')

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Про нас'
        verbose_name_plural = 'Про нас'
