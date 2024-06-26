# Generated by Django 4.2.6 on 2024-04-26 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('some_of_product', '0005_alter_featured_category_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('discount', models.FloatField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='some_of_product/media/image')),
            ],
        ),
        migrations.DeleteModel(
            name='feature_product',
        ),
        migrations.DeleteModel(
            name='ReadyOfOrder',
        ),
    ]
