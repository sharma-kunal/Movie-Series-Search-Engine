from django.db import models
from jsonfield import JSONField


class Data(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    movie = models.BooleanField(default=False)
    year = models.CharField(max_length=50, null=True)
    image = models.URLField(null=True)

    def __str__(self):
        return self.id


class MovieData(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    title = models.CharField(max_length=100)
    rating = models.FloatField()
    no_of_users_rated = models.IntegerField()
    status = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    summary = models.TextField(max_length=1000)
    genres = models.TextField(max_length=1000, null=True)
    images = JSONField(null=True, blank=True)
    cast = JSONField(null=True, blank=True)
    crew = JSONField(null=True, blank=True)
    reviews = JSONField(null=True, blank=True)
    recommendations = JSONField(null=True, blank=True)
    platforms = JSONField(null=True)
    platforms_present = models.BooleanField(default=False)

    def __str__(self):
        return self.id


class SeriesData(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    title = models.CharField(max_length=100)
    rating = models.FloatField()
    no_of_users_rated = models.IntegerField()
    date = models.CharField(max_length=50)
    summary = models.TextField(max_length=1000)
    genres = models.TextField(max_length=1000, null=True, blank=True)
    seasons = models.IntegerField()
    images = JSONField(null=True, blank=True)
    cast = JSONField(null=True, blank=True)
    crew = JSONField(null=True, blank=True)
    reviews = JSONField(null=True, blank=True)
    recommendations = JSONField(null=True, blank=True)
    platforms = JSONField(null=True)
    platforms_present = models.BooleanField(default=False)

    def __str__(self):
        return self.id