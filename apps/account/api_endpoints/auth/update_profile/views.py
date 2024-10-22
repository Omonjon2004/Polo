
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.account.api_endpoints.auth.update_profile.serializers import ProfileUpdateSerializers
from apps.account.models import Users


class ProfileUpdateViewSet(viewsets.ViewSet):
    queryset = Users.objects.all().order_by('id')
    serializer_class = ProfileUpdateSerializers
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        account =get_object_or_404(Users, pk=self.request.user.id)
        serializer = ProfileUpdateSerializers(account, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


__all__ = ["ProfileUpdateViewSet",]