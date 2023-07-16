# Generated by Django 4.2.2 on 2023-07-16 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48, verbose_name='Імя')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/%Y/%m/%d', verbose_name='Лого')),
                ('address', models.CharField(blank=True, max_length=256, verbose_name='Адресса')),
                ('email', models.EmailField(blank=True, max_length=48, null=True, verbose_name='Електронна пошта')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('short_description', models.TextField(max_length=512, verbose_name='Короткий опис')),
                ('description', models.TextField(max_length=2048, verbose_name='Довгий опис')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]