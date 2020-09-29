from django.db import models


class Main_categorie(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    code_id = models.BigIntegerField()
    product_name = models.CharField(max_length=20)
    image_url = models.URLField(max_length=200)
    category = models.ForeignKey(Main_categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
