# Generated by Django 4.2.6 on 2024-04-22 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('power_and_accessories', '0006_powerandaccessoriesdescriptionmodel_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cableandinternconnect',
            options={'verbose_name': 'cable And internconnect', 'verbose_name_plural': ' cable And Internconnect'},
        ),
        migrations.AlterModelOptions(
            name='cableandinternconnectproductadd',
            options={'ordering': ['price'], 'verbose_name': 'cable And internconnect ProductAdd', 'verbose_name_plural': 'Cable And Internconnect ProductAdds'},
        ),
        migrations.AlterModelOptions(
            name='powerandaccessories',
            options={'verbose_name': 'power And accessories', 'verbose_name_plural': 'power And Accessories'},
        ),
        migrations.AlterModelOptions(
            name='powerandaccessoriesdescriptionmodel',
            options={'verbose_name': 'powerAndaccessoriesDescriptionModel', 'verbose_name_plural': 'Power And Accessories Descriptions'},
        ),
        migrations.AlterModelOptions(
            name='powerandaccessoriesspecificaionmodel',
            options={'verbose_name': 'PowerAndaccessoriesSpecificaionModel', 'verbose_name_plural': 'Power And Accessories Specificaions'},
        ),
    ]
