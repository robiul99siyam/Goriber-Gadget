# Generated by Django 4.2.6 on 2024-04-16 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_and_wearable', '0004_fitness_and_wearable_product_quentity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fitness_and_wearable_product',
            old_name='productBrand',
            new_name='productBrandModel',
        ),
    ]