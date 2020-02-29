# models.py

from django.db import models
class CrudUser(models.Model):
  funame = models.CharField(max_length=30, blank=True)
  fupass = models.CharField(max_length=100, blank=True)
  cncip = models.FloatField(blank=True, null=True)
  cncuser=models.CharField(max_length=100, blank=True)
  monitoringport = models.IntegerField(blank=True,null=True)
  username = models.CharField(max_length=30, blank=True)

