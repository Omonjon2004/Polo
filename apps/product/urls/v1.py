from django.urls import path
from apps.product.api_endpoints import shoes, dress, jewelry, jackets

urlpatterns = [
    path('shoes/', shoes.ShoesListCreateAPIView.as_view(), name='shoes'),
    path('shoes/<int:pk>/', shoes.ShoesRetrieveUpdateDestroyAPIView.as_view(), name='shoes-detail'),
    path('dress/', dress.DressListCreateAPIView.as_view(), name='dress'),

    path('dress/<int:pk>/', dress.DressRetrieveUpdateDestroyAPIView.as_view(), name='dress-detail'),

    path('jewelry/', jewelry.JewelryListCreateAPIView.as_view(), name='jewelry'),
    path('jewelry/<int:pk>/', jewelry.JewelryRetrieveUpdateDestroyAPIView.as_view(), name='jewelry-detail'),
path('jackets/', jackets.JacketsListCreateAPIView.as_view(), name='jackets'),
    path('jackets/<int:pk>/', jackets.JacketsRetrieveUpdateDestroyAPIView.as_view(), name='jackets-detail'),

]
