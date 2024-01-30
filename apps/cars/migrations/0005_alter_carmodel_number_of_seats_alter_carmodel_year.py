# Generated by Django 5.0.1 on 2024-01-30 09:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_carmodel_model_alter_carmodel_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='number_of_seats',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.IntegerField(),
        ),
    ]
