# Generated by Django 4.2.6 on 2024-04-24 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sound_equipment', '0004_sounddescriptionmodel_soundspecificaionmodel_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sounddescriptionmodel',
            options={'verbose_name': 'soundDescriptionModel', 'verbose_name_plural': 'sound And Descriptions'},
        ),
        migrations.AlterModelOptions(
            name='soundspecificaionmodel',
            options={'verbose_name': 'soundSpecificaionModel', 'verbose_name_plural': 'sound And  Specificaion'},
        ),
    ]