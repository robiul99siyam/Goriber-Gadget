# Generated by Django 4.2.6 on 2024-03-23 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conver_and_glass', '0005_productbrand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverandglassproduct',
            name='productBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conver_and_glass.productbrand'),
        ),
    ]
