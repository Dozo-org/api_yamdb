from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "role", "confirmation_code")


admin.site.register(CustomUser, CustomUserAdmin)
