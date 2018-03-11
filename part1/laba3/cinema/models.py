from django.db import models

# Create your models here.

class Seance(models.Model):
    name = models.CharField(max_length=200)
    time = models.IntegerField()
    show_n = models.BooleanField(default=False)
    about = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Cinema(models.Model):
    title = models.CharField(max_length=200)
    seats = models.IntegerField()
    seance = models.ForeignKey(Seance , default=None)
    city = models.ForeignKey(City , default=None)

    def __str__(self):
        return self.title