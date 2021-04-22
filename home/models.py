from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    message = models.TextField()