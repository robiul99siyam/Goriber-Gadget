# Generated by Django 4.2.6 on 2024-03-23 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conver_and_glass', '0006_coverandglassproduct_productbrand'),
        ('peripheries', '0003_peripheries_delete_laptob_and_destop'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='peripheries',
            new_name='peripheriesProduct',
        ),
    ]