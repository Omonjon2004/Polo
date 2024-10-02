from django.contrib.postgres.search import TrigramSimilarity

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from apps.product.api_endpoints.bag.serializers import BagSerializer
from apps.product.models import Bags


class BagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bags.objects.all()
    serializer_class = BagSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        brand = self.request.query_params.get('brand')
        color = self.request.query_params.get('color')
        category = self.request.query_params.get('category')
        name = self.request.query_params.get('name')
        gender = self.request.query_params.get('gender')
        price = self.request.query_params.get('price')

        if brand:
            queryset = queryset.annotate(sim=TrigramSimilarity('brand', brand)).filter(sim__gte=0.2).order_by('sim')
        if color:
            queryset = queryset.annotate(sim=TrigramSimilarity('color', color)).filter(sim__gte=0.2).order_by('sim')
        if category:
            queryset = queryset.annotate(sim=TrigramSimilarity('category', category)).filter(sim__gte=0.2).order_by(
                'sim')
        if name:
            queryset = queryset.annotate(sim=TrigramSimilarity('name', name)).filter(sim__gte=0.2).order_by('sim')
        if gender:
            queryset = queryset.annotate(sim=TrigramSimilarity('gender', gender)).filter(sim__gte=0.2).order_by('sim')
        if price:
            queryset = queryset.annotate(sim=TrigramSimilarity('price', price)).filter(sim__gte=0.2).order_by('sim')
        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("brand", openapi.IN_QUERY, description="Filter by brand", type=openapi.TYPE_STRING),
            openapi.Parameter("color", openapi.IN_QUERY, description="Filter by color", type=openapi.TYPE_STRING),
            openapi.Parameter("category", openapi.IN_QUERY, description="Filter by category", type=openapi.TYPE_STRING),
            openapi.Parameter("name", openapi.IN_QUERY, description="Filter by name", type=openapi.TYPE_STRING),
            openapi.Parameter("gender", openapi.IN_QUERY, description="Filter by gender", type=openapi.TYPE_STRING),
            openapi.Parameter("price", openapi.IN_QUERY, description="Filter by price", type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BagRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bags.objects.all()
    serializer_class = BagSerializer
