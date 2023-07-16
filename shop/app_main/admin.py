from django.contrib import admin

from app_main.models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'address', 'email', 'phone', 'created_at', 'updated_at')
    list_display_links = ('pk', 'name')
    readonly_fields = ('updated_at', 'created_at')