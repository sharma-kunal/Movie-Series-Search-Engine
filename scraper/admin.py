from django.contrib import admin
from .models import Data, MovieData, SeriesData
# Register your models here.

admin.site.register(Data)
admin.site.register(MovieData)
admin.site.register(SeriesData)
