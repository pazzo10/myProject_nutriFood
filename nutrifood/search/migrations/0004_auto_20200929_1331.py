# Generated by Django 3.1.1 on 2020-09-29 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_remove_products_ingredient_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='code_id',
            field=models.BigIntegerField(),
        ),
    ]
