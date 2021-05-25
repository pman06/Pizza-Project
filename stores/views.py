from rest_framework import generics
from stores.models import Pizzeria
from stores.serializers import (PizzeriaListSerializer,
                                PizzeriaDetailSerializer,
                                )


class PizzeriaListAPIView(generics.ListAPIView):
    """List view for Pizzeria listing"""
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaListSerializer


class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
    """Detail view for Pizzeria details"""
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer
    lookup_field = "id"


class PizzeriaCreateAPIView(generics.CreateAPIView):
    """Create view for a pizzeria"""
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer


class PizzeriaUpdateAPIView(generics.RetrieveUpdateAPIView):
    """Update view for pizzeria"""
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer
    lookup_field = 'id'


class PizzeriaDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer
    lookup_field = 'id'
