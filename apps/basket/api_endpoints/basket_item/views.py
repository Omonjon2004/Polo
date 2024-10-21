from rest_framework import viewsets

from apps.basket.api_endpoints.basket_item.serializers \
    import BasketItemSerializer
from apps.basket.models import BasketItem


class BasketItemViewSet(viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer

    def get_queryset(self):
        # Agar basket id'siga qarab filterlashni istasangiz
        basket_id = self.kwargs.get('basket_id')
        if basket_id:
            return self.queryset.filter(basket_id=basket_id)
        return super().get_queryset()
