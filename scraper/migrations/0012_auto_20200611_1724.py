# Generated by Django 3.0.7 on 2020-06-11 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0011_auto_20200611_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='platforms_present',
            field=models.BooleanField(default=False),
        ),
    ]
