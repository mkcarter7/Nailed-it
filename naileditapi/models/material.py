from django.db import models

class Material(models.Model):
  
  name = models.CharField(max_length=50)
  description = models.TextField(blank=True, null=True)
  uid = models.CharField(max_length=30)
