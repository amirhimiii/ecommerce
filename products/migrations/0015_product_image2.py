# Generated by Django 4.0.6 on 2022-07-31 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, default=None, upload_to='image/'),
        ),
    ]
