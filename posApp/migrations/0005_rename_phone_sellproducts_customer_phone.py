# Generated by Django 3.2 on 2021-07-03 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0004_auto_20210703_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellproducts',
            old_name='phone',
            new_name='customer_phone',
        ),
    ]
