# Generated by Django 4.2.6 on 2024-03-23 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conver_and_glass', '0003_coverandglassproduct_coverandglass'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverandglassproduct',
            name='brand',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
