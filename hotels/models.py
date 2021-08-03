from django.db import models

# Create your models here.


class Hotel(models.Model):
    city = models.CharField(max_length=30)  # city acronym
    region = models.CharField(max_length=40)  # city region
    name = models.CharField(max_length=100)  # hotel name

    def __str__(self):
        return str(self.name)


class City(models.Model):
    acronym = models.CharField(max_length=40)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
