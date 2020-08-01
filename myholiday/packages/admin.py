from django.contrib import admin
from .models import Package, Category

# Register your models here.

class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'destination',
        'departs',
        'category',
        'price',
        'rating',
        'image',
        'image_url',
        'cover',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Package, PackageAdmin)
admin.site.register(Category, CategoryAdmin)
