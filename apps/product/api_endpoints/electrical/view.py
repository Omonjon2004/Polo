from rest_framework import generics

from apps.product.api_endpoints.electrical.serializers import ElectricalSerializer
from apps.product.models import Electrical


class ElectricalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Electrical.objects.all()
    serializer_class = ElectricalSerializer




class ElectricalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Electrical.objects.all()
    serializer_class = ElectricalSerializer



__all__=['ElectricalListCreateAPIView','ElectricalRetrieveUpdateDestroyAPIView']