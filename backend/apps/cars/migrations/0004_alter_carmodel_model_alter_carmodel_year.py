# Generated by Django 5.0.1 on 2024-01-30 08:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_rename_auto_park_carmodel_auto_parks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='model',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinLengthValidator(1980), django.core.validators.MaxLengthValidator(2024)]),
        ),
    ]