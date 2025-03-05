from django.db import models
from django.core.validators import MinValueValidator
#KEEPS VALUE FROM BEING BELOW ZERO
from .room import Room

class Project(models.Model):
  #on_delete=models.CASCADE DELETES ALL PROJECTS RELATED WHEN A ROOM IS DELETED
  #related_name="projects" ALLOWS YOU TO ACCESS ALL PROJECTS RELATED TO A ROOM
  name = models.CharField(max_length=50, null=False, blank=False)
  description = models.TextField(blank=True, null=True)
  #blank=True ALLOWS SUBMITTING WITHOUT DESCRIPTION
  #null=True ALLOWS AN EMPTY FIELD
  date_started = models.DateTimeField(null=True, blank=True)
  finish_time = models.DateTimeField(null=True, blank=True)
  estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="projects")
  uid = models.CharField(max_length=30, null=False, blank=False)
  materials = models.TextField(blank=True, null=True)

  #STORES FIREBASE UID
