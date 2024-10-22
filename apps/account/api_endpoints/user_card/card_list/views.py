from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.account.api_endpoints.user_card.card_list.serializers \
    import CardListSerializer
from apps.account.models import UsersCards


class CardListView(ListAPIView):
    serializer_class = CardListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UsersCards.objects.filter(account=self.request.user)
