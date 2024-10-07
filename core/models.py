from django.db import models

# Create your models here.

class Division(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=200, unique=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubDistrict(models.Model):
    name = models.CharField(max_length=200, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name