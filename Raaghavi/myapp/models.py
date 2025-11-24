from django.db import models
from django.contrib import admin
class product(models.Model):
    Productcode=models.CharField(primary_key=True,max_length=20)
    Name=models.CharField(max_length=30)
    Description=models.TextField()
    Price=models.FloatField()
    Design=models.CharField(max_length=20)
    Colour=models.CharField(max_length=15)
    Stock=models.IntegerField()
    Email=models.EmailField()

class productAdmin(admin.ModelAdmin):
    list_display=["Productcode","Name","Description","Price","Design","Colour","Stock","Email"]

