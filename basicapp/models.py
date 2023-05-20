from django.db import models

# Create your models here.

# class NewUsers(models.Model):
#     UserName=
class users(models.Model):
        name=models.CharField(max_length=90)
        email=models.EmailField()

