# Generated by Django 4.2.6 on 2024-04-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_and_tablet', '0005_phone_and_tabletproductadd_quentity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone_and_tabletproductadd',
            name='quentity',
        ),
        migrations.AddField(
            model_name='phone_and_tabletproductadd',
            name='status',
            field=models.CharField(blank=True, choices=[('In Stock ', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=40, null=True),
        ),
    ]
