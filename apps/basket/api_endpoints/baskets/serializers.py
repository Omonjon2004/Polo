from rest_framework import serializers

from apps.basket.models import BasketItem, Basket


class BasketItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    product_price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = BasketItem
        fields = ['product', 'quantity', 'product_price', 'total_price', 'added_at']

    def get_product(self, obj):
        # `get_product` methodini chaqiramiz va mahsulot nomini olamiz
        product = obj.get_product()
        return str(product) if product else None

    def get_product_price(self, obj):
        # Mahsulot narxini aniqlaymiz, har bir modelda `price` maydoni mavjud deb hisoblaymiz
        product = obj.get_product()
        if product:
            return product.price  # Barcha mahsulotlar narxni saqlashini kutamiz
        return 0

    def get_total_price(self, obj):
        # Jami narxni hisoblaymiz: quantity * product_price
        product_price = self.get_product_price(obj)
        return obj.quantity * product_price


class BasketSerializer(serializers.ModelSerializer):
    items = BasketItemSerializer(many=True)

    class Meta:
        model = Basket
        fields = ['user', 'created_at', 'items']
