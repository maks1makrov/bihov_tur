from django.contrib.auth.models import User
from django.db import models


class Field_of_activity(models.Model):
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)


class Toursites(models.Model):
    field_of_activity = models.ManyToManyField(Field_of_activity, related_name='toursites')
    name = models.CharField(max_length=100)
    status_choices = [
        ('act', 'active'),
        ('inact', 'inactive')
    ]
    status = models.CharField(max_length=50, choices=status_choices)
    discriptions = models.TextField()
    coordinates = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Photo_toursites(models.Model):
    photo = models.CharField(max_length=100)
    toursites_id = models.ForeignKey(Toursites, on_delete=models.CASCADE, related_name='photo_toursites')


class Enterpreneurs(models.Model):
    name = models.CharField(max_length=100)
    discriptions = models.TextField()
    email = models.EmailField()
    status_choices = [
        ('act', 'active'),
        ('inact', 'inactive')
    ]
    status = models.CharField(max_length=50, choices=status_choices)
    address = models.CharField(max_length=100)
    toursites_id = models.ManyToManyField(Toursites, related_name='enterpreneurs_toursites')

class Photo_enterpreneurs(models.Model):
    photo = models.CharField(max_length=100)
    enterpreneurs_id = models.ForeignKey(Enterpreneurs, on_delete=models.CASCADE, related_name='photo_enterpreneurs')


class Articles(models.Model):
    title = models.CharField(max_length=50)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_create = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.CharField(max_length=100)  # разобраться с картинками
    enterpreneurs_id = models.ManyToManyField(Enterpreneurs,
                                              related_name='articles_enterpreneurs')
    toursites_id = models.ManyToManyField(Toursites, related_name='articles_toursites')
