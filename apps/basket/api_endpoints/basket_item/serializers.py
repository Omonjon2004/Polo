from rest_framework import serializers

from apps.basket.models import BasketItem


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ['id',
                  'bag',
                  'shoes',
                  'dress',
                  'jewelry',
                  'quantity',
                  'added_at']
