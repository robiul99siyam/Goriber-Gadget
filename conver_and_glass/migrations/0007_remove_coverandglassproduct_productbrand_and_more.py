# Generated by Django 4.2.6 on 2024-03-24 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conver_and_glass', '0006_coverandglassproduct_productbrand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coverandglassproduct',
            name='productBrand',
        ),
        migrations.AddField(
            model_name='coverandglassproduct',
            name='productBrand',
            field=models.ManyToManyField(blank=True, null=True, to='conver_and_glass.productbrand'),
        ),
    ]
