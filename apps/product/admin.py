from django.contrib import admin
from apps.product.models \
    import \
    Shoes, Dress, Jackets, Jewelry, Electrical, Bags, Category, Brand, Color


class CommonProductAdmin(admin.ModelAdmin):
    list_display = ('brand',
                    'name',
                    'gender',
                    'color',
                    'season',
                    'category',
                    'price')
    list_filter = ('brand',
                   'gender',
                   'color',
                   'season',
                   'category',
                   'price')
    search_fields = ('brand',
                     'name',
                     'gender')
    ordering = ('-price',
                'name')

    def get_list_display(self, request):
        if hasattr(self.model, 'size'):
            return self.list_display + ('size',)
        return self.list_display

    def get_list_filter(self, request):
        if hasattr(self.model, 'size'):
            return self.list_filter + ('size',)
        return self.list_filter


admin.site.register(Shoes, CommonProductAdmin)
admin.site.register(Dress, CommonProductAdmin)
admin.site.register(Jackets, CommonProductAdmin)
admin.site.register(Jewelry, CommonProductAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Electrical)
class ElectricalAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'brand',
        'category'
    ]


@admin.register(Bags)
class BagsAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'price',
                    'brand',
                    'category'
                    ]
