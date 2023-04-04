from django.contrib import admin
from home.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(Product,ProductAdmin)