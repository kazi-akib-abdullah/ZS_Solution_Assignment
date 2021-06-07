from django.contrib import admin
from django.db import models
from rest_framework.serializers import LIST_SERIALIZER_KWARGS

# Register your models here.
from .models import Country, State, Address

class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'latitude', 'longitude', 'code']
    list_filter = ['name', 'code']

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ['name']

    def country(self, obj):
        return obj.name
    

class AdressAdmin(admin.ModelAdmin):
    list_display = ['name', 'house_number', 'road_number', 'state']
    list_filter = ['house_number', 'road_number']
    def state(self, obj):
        return obj.name


admin.site.site_header = 'Admin Dashboard'
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Address, AdressAdmin)