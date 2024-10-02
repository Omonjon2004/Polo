from django.urls import path
from apps.product.api_endpoints import shoes, dress, jewelry, jackets, electrical, bag

from django.views.decorators.cache import cache_page
from django.urls import path

urlpatterns = [
    path('shoes/', cache_page(60 * 15)(shoes.ShoesListCreateAPIView.as_view()), name='shoes'),
    path('shoes/<int:pk>/', shoes.ShoesRetrieveUpdateDestroyAPIView.as_view(), name='shoes-detail'),

    path('dress/', dress.DressListCreateAPIView.as_view(), name='dress'),
    path('dress/<int:pk>/', dress.DressRetrieveUpdateDestroyAPIView.as_view(), name='dress-detail'),

    path('jewelry/', jewelry.JewelryListCreateAPIView.as_view(), name='jewelry'),
    path('jewelry/<int:pk>/', jewelry.JewelryRetrieveUpdateDestroyAPIView.as_view(), name='jewelry-detail'),

    path('jackets/', jackets.JacketsListCreateAPIView.as_view(), name='jackets'),
    path('jackets/<int:pk>/', jackets.JacketsRetrieveUpdateDestroyAPIView.as_view(), name='jackets-detail'),

    path('electrical/', electrical.ElectricalListCreateAPIView.as_view(), name='electrical'),
    path('electrical/<int:pk>/', electrical.ElectricalRetrieveUpdateDestroyAPIView.as_view(), name='electrical-detail'),

    path('bag/', cache_page(60 * 15)(bag.BagListCreateAPIView.as_view()), name='bag'),
    path('bag/<int:pk>/', bag.BagRetrieveUpdateDestroyAPIView.as_view(), name='bag-detail'),
]
