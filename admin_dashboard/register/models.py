from django.db import models

# Create your models here.
class contact(models.Model):
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=20)
    address = models.TextField()