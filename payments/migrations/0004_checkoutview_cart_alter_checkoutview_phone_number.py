# Generated by Django 4.0.6 on 2022-07-30 07:42

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0002_alter_cartitem_quantity'),
        ('payments', '0003_alter_checkoutview_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutview',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='process.cart'),
        ),
        migrations.AlterField(
            model_name='checkoutview',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='e.g:0912 123 4567', max_length=14, region=None),
        ),
    ]
