from apps.basket.models import BasketItem
from .serializers import BasketItemSerializer
from rest_framework import viewsets
from apps.basket.tasks import update_stock


class BasketItemViewSet(viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer

    def perform_create(self, serializer):
        basket_item = serializer.save()

        if basket_item.bag:
            product_type = 'bag'
            product_id = basket_item.bag.id
        elif basket_item.shoes:
            product_type = 'shoes'
            product_id = basket_item.shoes.id
        elif basket_item.dress:
            product_type = 'dress'
            product_id = basket_item.dress.id
        elif basket_item.jewelry:
            product_type = 'jewelry'
            product_id = basket_item.jewelry.id
        else:
            return

        update_stock.delay(product_type, product_id, basket_item.quantity)

    def perform_update(self, serializer):
        basket_item = serializer.save()

        if basket_item.bag:
            product_type = 'bag'
            product_id = basket_item.bag.id
        elif basket_item.shoes:
            product_type = 'shoes'
            product_id = basket_item.shoes.id
        elif basket_item.dress:
            product_type = 'dress'
            product_id = basket_item.dress.id
        elif basket_item.jewelry:
            product_type = 'jewelry'
            product_id = basket_item.jewelry.id
        else:
            return

        update_stock.delay(product_type, product_id, basket_item.quantity)


__all__ = ['BasketItemViewSet']
