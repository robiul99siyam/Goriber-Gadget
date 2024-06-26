# Generated by Django 4.2.6 on 2024-04-19 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone_and_tablet', '0007_specificationmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescriptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='phone_and_tablet/media/image')),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='specificationmodel',
            name='CPU',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='specificationmodel',
            name='chipset',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='phone_and_tabletproductadd',
            name='DescriptionModel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phone_and_tablet.descriptionmodel'),
        ),
    ]
