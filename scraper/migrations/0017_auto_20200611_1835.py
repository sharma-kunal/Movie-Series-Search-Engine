# Generated by Django 3.0.7 on 2020-06-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0016_seriesdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='genres',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='seriesdata',
            name='genres',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
