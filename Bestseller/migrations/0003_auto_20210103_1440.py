# Generated by Django 3.1.2 on 2021-01-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bestseller', '0002_bestseller_is_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestseller',
            name='is_publish',
            field=models.BooleanField(default=0),
        ),
    ]
