# Generated by Django 3.0.6 on 2020-05-16 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0004_cart_quanity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='quanity',
            new_name='quantity',
        ),
    ]
