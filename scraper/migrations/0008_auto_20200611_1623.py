# Generated by Django 3.0.7 on 2020-06-11 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0007_auto_20200611_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
