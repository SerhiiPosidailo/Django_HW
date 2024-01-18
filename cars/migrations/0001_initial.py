# Generated by Django 5.0.1 on 2024-01-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('number_of_seats', models.IntegerField()),
                ('body_type', models.CharField(max_length=20)),
                ('engine_capacity', models.FloatField()),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
