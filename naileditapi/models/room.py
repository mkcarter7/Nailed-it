from django.db import models

class Room(models.Model):
  
  name = models.CharField(max_length=50)
  description = models.TextField()
  image = models.URLField(blank=True, null=True)
  #blank=True FIELD IS OPTIONAL IN FORMS
  #NULL=tRUE FIELD CAN BE BLANK IN DATABASE
  uid = models.CharField(max_length=30)
