# Generated by Django 3.1.4 on 2021-01-03 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stories', '0002_remove_stories_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='publish_date',
            field=models.DateField(null=True),
        ),
    ]
