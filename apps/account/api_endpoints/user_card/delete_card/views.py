from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from apps.account.api_endpoints.user_card.delete_card.serializers import DeleteCardSerializer
from apps.account.models import UsersCards


class DeleteCardView(DestroyAPIView):
    queryset = UsersCards.objects.all()
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        serializer = DeleteCardSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        card_id = serializer.validated_data['card_id']

        try:
            card = UsersCards.objects.get(id=card_id)
        except UsersCards.DoesNotExist:
            raise NotFound("Card not found.")

        if card.account != request.user:
            return Response({"detail": "You do not have permission to delete this card."}, status=status.HTTP_403_FORBIDDEN)

        card.delete()
        return Response({"detail": "Card deleted successfully."}, status=status.HTTP_200_OK)
