from django.contrib.auth.models import User
from django.db import models


class MSP(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msp_to_user')
    contact_info = models.CharField(max_length=50)
    services = models.CharField(max_length=100)


class Tourists_objects(models.Model):
    msp = models.ForeignKey(MSP, on_delete=models.CASCADE, related_name="tour_to_msp", blank=True, null=True)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=100) # разобраться с картинками
    address = models.CharField(max_length=100)
    coordinates = models.CharField(
        max_length=100)  # надо переделать под гео джанго coords = gis_models.PointField(u"долгота/широта", srid=4326, blank=True, null=True)
    description = models.TextField()


class Article(models.Model):
    title = models.CharField(max_length=50)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_create = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    short_text = models.CharField(max_length=150)
    image = models.CharField(max_length=100) # разобраться с картинками
    on_tour_objects = models.ManyToManyField(Tourists_objects)
    on_MSP = models.ManyToManyField(MSP)

