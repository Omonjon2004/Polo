from rest_framework import serializers

from apps.account.models import UsersCards


class DeleteCardSerializer(serializers.Serializer):
    card_id = serializers.IntegerField()

    class Meta:
        model = UsersCards
