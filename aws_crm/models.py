from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    aws_access_key_id = models.CharField(max_length=100)
    aws_secret_access_key = models.CharField(max_length=100)