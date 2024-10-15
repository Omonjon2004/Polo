from rest_framework import viewsets

from apps.basket.api_endpoints.baskets.serializers import BasketSerializer
from apps.basket.models import Basket


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer