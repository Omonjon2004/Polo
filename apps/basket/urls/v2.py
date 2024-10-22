from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.basket.api_endpoints.basket_item.views import BasketItemViewSet
from apps.basket.api_endpoints.baskets.views import BasketViewSet

router = DefaultRouter()
router.register(r'basket_item', BasketItemViewSet, basename='basketitem')
router.register(r'basket', BasketViewSet, basename='basket')

urlpatterns = router.urls
