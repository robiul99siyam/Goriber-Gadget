# Generated by Django 4.2.6 on 2024-04-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peripheries', '0005_peripheriesproduct_perpheries'),
    ]

    operations = [
        migrations.AddField(
            model_name='peripheriesproduct',
            name='quentity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
