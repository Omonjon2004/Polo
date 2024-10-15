from django.contrib import admin
from apps.product.models import Shoes, Dress, Jackets, Jewelry, Electrical, Bags


class CommonProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'gender', 'size', 'color', 'season', 'category', 'price')
    list_filter = ('brand', 'gender', 'size', 'color', 'season', 'category', 'price')
    search_fields = ('brand', 'name', 'gender')
    ordering = ('-price', 'name')


admin.site.register(Shoes, CommonProductAdmin)
admin.site.register(Dress, CommonProductAdmin)
admin.site.register(Jackets, CommonProductAdmin)
admin.site.register(Jewelry, CommonProductAdmin)

@admin.register(Electrical)
class ElectricalAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','brand','category']

@admin.register(Bags)
class BagsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'brand', 'category']




