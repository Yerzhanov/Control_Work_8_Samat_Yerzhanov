from django.contrib import admin

from products.models import ProductCategory, Product, Review

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    fields = ('name', 'description', 'price', 'image', 'category')
    search_fields = ('name',)
    ordering = ('-name', )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', )
    fields = ('user', 'description', 'rating')
    search_fields = ('product',)
    ordering = ('-product', )
