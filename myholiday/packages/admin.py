from django.contrib import admin
from .models import Package, Category, Comment

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

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'package',
        'submitted_at',
        'text',
        'active',
    )
    list_filter = (
        'active',
        'package',
        'user',
        'submitted_at',
    )
    search_fields = (
        'user',
        'package',
        'submitted_at',
        'active'
    )
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Package, PackageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
