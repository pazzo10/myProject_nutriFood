from django.db import models


class Main_categories(models.Model):
    category_name = models.CharField(max_length=20)


class Products(models.Model):
    code_id = models.CharField(max_length=200)
    product_name = models.CharField(max_length=20)
    ingredient_text = models.CharField(max_length=200)
    image_url = models.URLField(max_length=200)
    category = models.ForeignKey(Main_categories, on_delete=models.CASCADE)
