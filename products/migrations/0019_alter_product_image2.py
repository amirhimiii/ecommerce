# Generated by Django 4.0.6 on 2022-08-03 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_product_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, default='image/117515975.jpg', null=True, upload_to='image/'),
        ),
    ]