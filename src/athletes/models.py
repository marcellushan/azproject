from django.db import models

from azproject.settings import BASE_DIR

# Create your models here.

class Year(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

class Family(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name
    

class Athlete(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    familys = models.ManyToManyField(Family)
    schools = models.ManyToManyField(School)
    years = models.ManyToManyField(Year)
    # photo = models.ImageField(upload_to )

    def __str__(self):
        return self.lname + ", " + self.fname


