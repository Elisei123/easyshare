from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class retele_de_socializare_utilizator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    github = models.CharField(max_length=40, null=True, default='https://github.com/')
    facebook = models.CharField(max_length=40, null=True, default='https://www.facebook.com/')
    instagram = models.CharField(max_length=40, null=True, default='https://www.instagram.com/')
    gmail = models.CharField(max_length=40, null=True, default='')
    youtube = models.CharField(max_length=40, null=True, default='https://www.youtube.com/channel/')
    linkedin = models.CharField(max_length=40, null=True, default='https://www.linkedin.com/in/')
    discord = models.CharField(max_length=40, null=True, default='')
    skype = models.CharField(max_length=40, null=True, default='')
    steam = models.CharField(max_length=40, null=True, default='https://steamcommunity.com/profiles/')
    paypal = models.CharField(max_length=40, null=True, default='https://www.paypal.me/')
