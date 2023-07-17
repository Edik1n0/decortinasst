# Generated by Django 4.1.5 on 2023-05-05 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productos", "0013_alter_product_productdiscount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="productdiscount",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="Valor de descuento"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="productoldprice",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="Precio normal"
            ),
        ),
    ]
