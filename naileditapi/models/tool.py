from django.db import models

class Tool(models.Model):
  
  name = models.CharField(max_length=50)
  description = models.TextField()
  uid = models.CharField(max_length=30)
