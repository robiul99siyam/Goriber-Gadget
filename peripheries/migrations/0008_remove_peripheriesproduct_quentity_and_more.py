# Generated by Django 4.2.6 on 2024-04-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peripheries', '0007_rename_productbrand_peripheriesproduct_productbrandmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peripheriesproduct',
            name='quentity',
        ),
        migrations.AddField(
            model_name='peripheriesproduct',
            name='status',
            field=models.CharField(blank=True, choices=[('In Stock ', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=40, null=True),
        ),
    ]
