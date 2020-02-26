from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class retele_de_socializare_utilizator(models.Model):
    github = models.CharField(max_length=40, null=True)
    facebook = models.CharField(max_length=40, null=True)
    instagram = models.CharField(max_length=40, null=True)
    gmail = models.CharField(max_length=40, null=True)
    youtube = models.CharField(max_length=40, null=True)
    linkedin = models.CharField(max_length=40, null=True)
    discord = models.CharField(max_length=40, null=True)
    skype = models.CharField(max_length=40, null=True)
    steam = models.CharField(max_length=40, null=True)
    paypal = models.CharField(max_length=40, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
