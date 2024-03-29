# Generated by Django 3.0.7 on 2020-06-11 17:58

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0014_auto_20200611_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='cast',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moviedata',
            name='crew',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moviedata',
            name='images',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moviedata',
            name='recommendations',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moviedata',
            name='reviews',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
