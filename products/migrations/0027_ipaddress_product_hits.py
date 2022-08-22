# Generated by Django 4.1 on 2022-08-21 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_product_vip'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='ip address')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', to='products.ipaddress'),
        ),
    ]