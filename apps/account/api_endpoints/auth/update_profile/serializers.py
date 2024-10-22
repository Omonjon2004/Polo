from rest_framework import serializers

from apps.account.models import Users


class ProfileUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name',
                  'last_name',
                  'phone_number']
