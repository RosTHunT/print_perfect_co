# Generated by Django 4.2.2 on 2023-07-25 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0003_rename_categories_product_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categories',
        ),
    ]