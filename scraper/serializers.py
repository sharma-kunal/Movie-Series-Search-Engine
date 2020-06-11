from rest_framework import serializers
from .models import Data, MovieData


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieData
        fields = '__all__'
