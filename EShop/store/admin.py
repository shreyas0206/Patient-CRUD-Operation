from django.contrib import admin
from .models import Product,Category,Order
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','category','description','image']
admin.site.register(Product,PostAdmin)

class PostCategory(admin.ModelAdmin):
    list_display = ['id','name']    
admin.site.register(Category,PostCategory)

class PostOrder(admin.ModelAdmin):
    list_display = ['id','user']    
    # search_fields=('user',)
    list_filter=('user',)
admin.site.register(Order,PostOrder)
