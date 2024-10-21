from rest_framework import serializers

from apps.product.models import Electrical


class ElectricalSerializer\
            (serializers.ModelSerializer):
    class Meta:
        model = Electrical
        fields = '__all__'
