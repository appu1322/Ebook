# Generated by Django 3.1.2 on 2021-01-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bestseller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestseller',
            name='is_publish',
            field=models.IntegerField(default=0),
        ),
    ]
