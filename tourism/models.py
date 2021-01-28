from django.contrib.auth.models import User
from django.db import models


class Field_of_activity(models.Model):
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Toursites(models.Model):
    field_of_activity = models.ManyToManyField(Field_of_activity, related_name='toursites')
    name = models.CharField(max_length=100)
    status_choices = [
        ('act', 'active'),
        ('inact', 'inactive')
    ]
    status = models.CharField(max_length=50, choices=status_choices)
    discription = models.TextField()
    coordinates = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Photo_toursites(models.Model):
    photo = models.CharField(max_length=100)
    toursite_id = models.ForeignKey(Toursites, on_delete=models.CASCADE, related_name='photo_toursite')


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
    toursite_id = models.ManyToManyField(Toursites, related_name='enterpreneur_toursite')

    def __str__(self):
        return self.name

class Photo_enterpreneurs(models.Model):
    photo = models.CharField(max_length=100)
    enterpreneur_id = models.ForeignKey(Enterpreneurs, on_delete=models.CASCADE, related_name='photo_enterpreneur')


class Links(models.Model):
    enterpreneur_id = models.ForeignKey(Enterpreneurs, on_delete=models.CASCADE, related_name='link_enterpreneur')
    link = models.CharField(max_length=100)


class Table(models.Model):
    enterpreneur_id = models.ForeignKey(Enterpreneurs, on_delete=models.CASCADE, related_name='table_enterpreneur')
    phone_number = models.CharField(max_length=150)

class Articles(models.Model):
    title = models.CharField(max_length=50)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_create = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.CharField(max_length=100, blank=True, null=True)
    status_choices = [
        ('pub', 'publish'),
        ('not_pub', 'not published')
    ]
    status = models.CharField(max_length=50, choices=status_choices)
    enterpreneur_id = models.ManyToManyField(Enterpreneurs,
                                              related_name='articles_enterpreneur')
    toursite_id = models.ManyToManyField(Toursites, related_name='articles_toursite')

    def __str__(self):
        return self.title