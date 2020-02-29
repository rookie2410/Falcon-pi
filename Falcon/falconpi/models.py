# models.py

from django.db import models
class CrudUser(models.Model):
  funame = models.CharField(max_length=30, blank=True)
  fupass = models.CharField(max_length=100, blank=True)
  cn = models.CharField( max_length=30, blank=True,)
  cncuser=models.CharField(max_length=100, blank=True)
  monitport = models.IntegerField(null=True)
  fuid = models.IntegerField(null=True)



      
        
        
        
        

