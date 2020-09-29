# Generated by Django 3.1 on 2020-09-29 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_auto_20200929_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpage',
            name='Primary_address_1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userpage',
            name='Primary_address_2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userpage',
            name='Primary_country',
            field=django_countries.fields.CountryField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='userpage',
            name='Primary_telephone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userpage',
            name='profile_county',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='userpage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
