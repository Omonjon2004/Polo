from rest_framework import serializers

from apps.basket.api_endpoints.basket_item.serializers import BasketItemSerializer
from apps.basket.models import Basket


class BasketSerializer(serializers.ModelSerializer):
    items = BasketItemSerializer(many=True, read_only=True)

    class Meta:
        model = Basket
        fields = ['id', 'user', 'created_at', 'items', 'total_price']