# Generated by Django 4.2.6 on 2024-04-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loptob_and_desktop', '0005_rename_laptob_and_destop_laptob_and_destop_productadd'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptob_and_destop_productadd',
            name='quentity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
