# Generated by Django 4.2.6 on 2024-04-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('power_and_accessories', '0004_cableandinternconnectproductadd_quentity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cableandinternconnectproductadd',
            name='quentity',
        ),
        migrations.AddField(
            model_name='cableandinternconnectproductadd',
            name='status',
            field=models.CharField(blank=True, choices=[('In Stock ', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=40, null=True),
        ),
    ]
