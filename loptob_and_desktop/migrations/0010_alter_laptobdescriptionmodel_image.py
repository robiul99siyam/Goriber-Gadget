# Generated by Django 4.2.6 on 2024-04-24 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loptob_and_desktop', '0009_alter_laptobdescriptionmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptobdescriptionmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='loptob_and_desktop/media/image'),
        ),
    ]