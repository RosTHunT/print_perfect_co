
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator


class PrimaryUser(AbstractUser):

    class Meta:
        ordering = ('first_name', )

    username_validator = UnicodeUsernameValidator()
    email_validators = EmailValidator()

    username = models.CharField(
        'username',
        max_length=150,
        unique=False,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists."
        },
        blank=True,
    )

    email = models.EmailField(
        'email',
        max_length=150,
        unique=True,
        db_index=True,
        error_messages={
            'unique': "A user with that email already exists."
        },
        validators=[email_validators],
        blank=False,
    )

    rating = models.PositiveIntegerField(default=0, blank=True, verbose_name='Рейтинг')
    dob = models.DateField(blank=True, null=True, verbose_name='Дата народження')
    city = models.CharField(max_length=64, blank=True, verbose_name='Місто')
    country = models.CharField(max_length=128, blank=True, verbose_name='Країна')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    photo = models.ImageField(upload_to='profile/photo/%Y/%m/%d/', blank=True, null=True, verbose_name='Фото')

    last_logout = models.DateTimeField('last logout', blank=True, null=True)
    email_verify = models.BooleanField(default=False, verbose_name='Верифікація')

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta(AbstractUser.Meta):
        abstract = False
