# Generated by Django 3.0.7 on 2020-06-11 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0017_auto_20200611_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seriesdata',
            name='genres',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
