# Generated by Django 4.2.6 on 2024-04-19 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone_and_tablet', '0009_alter_phone_and_tabletproductadd_descriptionmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone_and_tabletproductadd',
            name='DescriptionModel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DescriptionModel', to='phone_and_tablet.descriptionmodel'),
        ),
        migrations.AlterField(
            model_name='phone_and_tabletproductadd',
            name='SpecificationModel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SpecificationModel', to='phone_and_tablet.specificationmodel'),
        ),
        migrations.AlterField(
            model_name='phone_and_tabletproductadd',
            name='ipadAndTAB',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ipadAndTAB', to='phone_and_tablet.ipadandtab'),
        ),
        migrations.AlterField(
            model_name='phone_and_tabletproductadd',
            name='phoneAndtablet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phoneAndtablet', to='phone_and_tablet.phoneandtablet'),
        ),
        migrations.AlterField(
            model_name='phone_and_tabletproductadd',
            name='productBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ipadAndTAB', to='phone_and_tablet.productbrand'),
        ),
    ]
