from django.db import models

# Create your models here.


class Products(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=1256)
    Price = models.IntegerField(default=0)
    ImageUrl = models.CharField(max_length=1256)

    def __str__(self):
        return self.Name


class Textile(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=1256)
    Price = models.IntegerField(default=0)
    ImageUrl = models.CharField(max_length=1256)

    def __str__(self):
        return self.Name
