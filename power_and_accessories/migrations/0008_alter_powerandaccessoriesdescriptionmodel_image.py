# Generated by Django 4.2.6 on 2024-04-25 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('power_and_accessories', '0007_alter_cableandinternconnect_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powerandaccessoriesdescriptionmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='power_and_accessories/media/image'),
        ),
    ]