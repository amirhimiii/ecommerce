# Generated by Django 4.1 on 2022-08-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_alter_articlehit_ip_address_alter_articlehit_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=7, verbose_name='price'),
        ),
    ]
