# Generated by Django 4.2.2 on 2023-07-10 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорію', 'verbose_name_plural': 'КатегоріЇ'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товари'},
        ),
    ]