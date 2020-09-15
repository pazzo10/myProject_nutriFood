from django.db import models

class Produit(models.Model):
    ingredient_text = models.CharField(max_length=200)
