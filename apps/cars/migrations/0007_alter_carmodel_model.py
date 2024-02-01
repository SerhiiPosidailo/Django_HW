# Generated by Django 5.0.1 on 2024-02-01 08:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_carmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='model',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{2,20}$', 'Only alphanumeric 2-20 characters.')]),
        ),
    ]
