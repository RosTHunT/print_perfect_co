from django.conf import settings
from django.contrib import admin, messages

from django.contrib.auth.forms import (AdminPasswordChangeForm, UserChangeForm, UserCreationForm,)

from django.utils.decorators import method_decorator

from django.utils.translation import gettext, gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from app_auth.forms import PrimaryUserCreationForm, PrimaryUserChangeForm
from app_auth.models import PrimaryUser

csrf_protect_m = method_decorator(csrf_protect)
sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())


@admin.register(PrimaryUser)
class UserAdmin(admin.ModelAdmin):
    # add_form_template = 'admin/auth/user/add_form.html'
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': (
            'phone', 'rating', 'dob', 'city', 'country', 'email_verify', 'first_name', 'last_name',
            'photo',
        )
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'last_logout', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    add_form = PrimaryUserCreationForm
    form = PrimaryUserChangeForm
    change_password_form = AdminPasswordChangeForm
    list_display = ('id', 'phone', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'email_verify')
    list_display_links = ('id', 'phone', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('phone', 'username', 'first_name', 'last_name', 'email')
    ordering = ('-id', )
    filter_horizontal = ('groups', 'user_permissions', )
