from rest_framework import serializers

from apps.product.models import Jewelry


class JewelrySerializer \
            (serializers.ModelSerializer):
    class Meta:
        model = Jewelry
        fields = '__all__'
