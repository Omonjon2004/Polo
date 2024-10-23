from django.contrib import admin

from apps.basket.models import Basket, BasketItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass

@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    pass