from country.models import Address, Country, State
from django.shortcuts import render
from rest_framework import generics
from .serializers import AddressSerializer, CountrySerializer, StateSerializer
Create your views here.

class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateList(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class AddressList(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

