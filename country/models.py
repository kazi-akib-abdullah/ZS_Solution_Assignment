from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    code = models.CharField(max_length=10)

class State(models.Model):
    name = models.CharField(max_length=100)
    select_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='Country')
    # def __str__(self):
    #     return "{}:{}..".format(self.name, self.select_country[:10])

class Address(models.Model):
    name = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20)
    road_number = models.IntegerField()
    select_state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='Stete')