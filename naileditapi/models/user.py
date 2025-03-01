from django.db import models


class User(models.Model):

    uid = models.CharField(max_length=50)#FIREBASE ID
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=75)
