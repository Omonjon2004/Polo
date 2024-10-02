from rest_framework import serializers

from apps.product.models import Dress


class JacketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dress
        fields = '__all__'