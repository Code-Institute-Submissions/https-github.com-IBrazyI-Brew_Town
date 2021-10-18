from django.contrib import admin
from .models import Category, Product

#Used to display the data of the products in an easy to read format within the database.
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


#Used to display both names for the categories within the database.
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        
    )



#Allows the admin to display the data and formating of the database.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)