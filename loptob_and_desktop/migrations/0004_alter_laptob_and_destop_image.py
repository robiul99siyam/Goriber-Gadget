# Generated by Django 4.2.6 on 2024-03-23 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loptob_and_desktop', '0003_remove_laptob_and_destop_imacandmacmini_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptob_and_destop',
            name='image',
            field=models.ImageField(upload_to='loptob_and_desktop/media/image'),
        ),
    ]
