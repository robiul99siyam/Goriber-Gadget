# Generated by Django 4.2.6 on 2024-04-16 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peripheries', '0007_rename_productbrand_peripheriesproduct_productbrandmodel'),
        ('fitness_and_wearable', '0005_rename_productbrand_fitness_and_wearable_product_productbrandmodel'),
        ('conver_and_glass', '0010_coverandglassproduct_quentity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='productBrand',
            new_name='productBrandModel',
        ),
    ]