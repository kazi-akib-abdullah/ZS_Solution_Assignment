from django.db.models import fields
from django.utils import tree
from rest_framework import serializers
from rest_framework.exceptions import _get_full_details
from rest_framework.utils.field_mapping import get_field_kwargs
from .models import Country, State, Address


class AddressSerializer(serializers.ModelSerializer):
    # country = CountrySerializer()
    # state = StateSerializer()
    class Meta:
        model = Address
        fields = '__all__'




class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    state_source = StateSerializer(many = True)
    address_source = AddressSerializer(many = True)
    class Meta:
        model = Country
        fields = '__all__'



    