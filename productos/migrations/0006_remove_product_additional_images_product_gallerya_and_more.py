# Generated by Django 4.1.5 on 2023-05-03 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productos", "0005_additionalimage_product_additional_images"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="additional_images",
        ),
        migrations.AddField(
            model_name="product",
            name="gallerya",
            field=models.ImageField(
                blank=True,
                upload_to="imagenes-decortinas/",
                verbose_name="Imagen secundaria del Producto",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="galleryb",
            field=models.ImageField(
                blank=True,
                upload_to="imagenes-decortinas/",
                verbose_name="Imagen final del Producto",
            ),
        ),
        migrations.DeleteModel(
            name="AdditionalImage",
        ),
    ]
