# Generated by Django 3.1 on 2020-09-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200922_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.DecimalField(choices=[(0.5, '500g'), (2, '2kg'), (1, '1kg'), (1.5, '1.5kg')], decimal_places=2, default=0.5, max_digits=6),
        ),
    ]