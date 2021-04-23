from django.contrib import admin
from import_export.admin import ImportMixin

from .models import Category, Genre, Title
from .resources import CategoryResource, GenreResource, TitleResource


class TitleAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = TitleResource


class GenreAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = GenreResource


class CategoryAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = CategoryResource


admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
