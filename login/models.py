from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    mail = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)