from django.db import models

# Create your models here.


class Cinema(models.Model):
    title = models.CharField(max_length=200, default=None)
    city = models.CharField(max_length=200, default=None)
    seats = models.IntegerField(default=0)



    def __str__(self):
        return  self.title

