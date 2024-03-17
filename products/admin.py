from django.contrib import admin
from .models import Product, Painting, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class PaintingAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'paint_type')
    list_filter = ('category', 'price', 'paint_type')
    search_fields = ('name', 'description', 'paint_type')
    readonly_fields = ('dimensions', 'weight')
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'price', 'paint_type')
        }),
        ('Image', {
            'fields': ('image', 'image_url'),
        }),
        ('Additional Information', {
            'fields': ('description', 'dimensions', 'weight'),
            'classes': ('collapse',)
        }),
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product)
admin.site.register(Painting)
admin.site.register(Category)
