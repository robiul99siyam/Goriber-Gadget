# Generated by Django 4.2.6 on 2024-03-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conver_and_glass', '0004_coverandglassproduct_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='productBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='coverandglassproduct',
            old_name='brand',
            new_name='product_code',
        ),
    ]