from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=100)
    provider = models.CharField(max_length=50, null=True)
    link = models.URLField(null=True)
    movie = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MovieData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    movie = models.BooleanField(default=False)
    year = models.CharField(max_length=5, null=True)
    image = models.URLField(null=True)

    def __str__(self):
        return self.name
