from django.db import models

# Create your models here.

class coders(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.EmailField(max_length=50)
    profilePic = models.ImageField(upload_to='profilePic',null=True, default=None)
    intro = models.CharField(max_length=1000, null=True, default=None)
    # location and timezone will be left null so far
    location = models.CharField(max_length=50, null=True, default=None)
    timezone = models.DateTimeField(null=True, default=None)



class clients(models.Model):
    username = models.CharField(max_length=100)
    location = models.CharField(max_length=50, null=True, default=None)
    timezone = models.DateTimeField(null=True, default=None)
    email = models.EmailField(max_length=50)