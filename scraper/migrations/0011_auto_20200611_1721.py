# Generated by Django 3.0.7 on 2020-06-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0010_auto_20200611_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='platforms_present',
            field=models.TextField(max_length=10),
        ),
    ]
