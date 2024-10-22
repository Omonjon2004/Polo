from rest_framework import serializers

from apps.account.models import UsersCards


class CardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersCards
        fields = ['id', 'card_name', 'card_number']
