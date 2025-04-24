from django.db import models

# Create your models here.
class Tokens_mercado_livre_correto(models.Model):
    
    filial = models.TextField()
    refresh_token = models.CharField(max_length=250)
    access_token = models.CharField(max_length=250)