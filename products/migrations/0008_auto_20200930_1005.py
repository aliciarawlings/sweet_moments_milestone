# Generated by Django 3.1 on 2020-09-30 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200930_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.DecimalField(choices=[(2, '2kg'), (1, '1kg'), (1.5, '1.5kg'), (0.5, '500g')], decimal_places=2, default=0.5, max_digits=6),
        ),
    ]
