from rest_framework import serializers

from apps.product.models import Bags


class BagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bags
        fields='__all__'


# class BagDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Bags
#         fields=['name','color','discount','price','brand','']