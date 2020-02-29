from django.contrib import admin

# Register your models here.

from django.db import models

# class CrudUser(models.Model):
#     name = models.CharField(max_length=30, blank=True)
#     address = models.CharField(max_length=100, blank=True)
#     age = models.IntegerField(blank=True, null=True)

from .models import CrudUser
admin.site.register(CrudUser)