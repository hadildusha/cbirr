# Generated by Django 4.2.1 on 2023-06-04 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbir_app', '0002_product_ran'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ran',
        ),
    ]
