# Generated by Django 4.2.6 on 2024-04-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('some_of_product', '0002_alter_feature_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bennersection',
            name='image',
            field=models.ImageField(upload_to='some_of_product/media/image/'),
        ),
    ]
