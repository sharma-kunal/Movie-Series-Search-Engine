from django.shortcuts import render
# import sys
import os
from .models import MovieData, SeriesData
# sys.path.append(os.path.abspath('../websites/crawlers'))
from websites.crawlers.airtel import airtel_movie, airtel_show
from websites.crawlers.alt_balaji import alt_balaji_movie, alt_balaji_show
from websites.crawlers.eros_now import eros_now_movie, eros_now_show
from websites.crawlers.idea import idea_movie, idea_show
from websites.crawlers.jio import jio_movie, jio_show
from websites.crawlers.mx_player import mx_player_movie, mx_player_show
from websites.crawlers.vodafone import vodafone_movie, vodafone_show
from websites.crawlers.zee5 import zee5_movie, zee5_show
from websites.crawlers.sony_liv import sony_liv_movie, sony_liv_show
from websites.crawlers.hotstar import hotstar_movie, hotstar_show
import requests
import json


image_url = "https://image.tmdb.org/t/p/original"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(BASE_DIR + '/../api-keys.txt', 'r') as f:
    di = json.load(f)

key = di['tmdb_api_key']


class MovieDetails:
    def __init__(self, id):
        self.details = {}
        self.get_data(id)

    def get_movies(self, id, year):
        name = self.details['title']
        data = [airtel_movie(name, id, year), alt_balaji_movie(name, id, year), eros_now_movie(name, id, year),
                idea_movie(name, id, year), jio_movie(name, id, year), mx_player_movie(name, id, year),
                vodafone_movie(name, id, year), zee5_movie(name, id, year), sony_liv_movie(name, id, year),
                hotstar_movie(name, id, year)]
        self.details['platforms'] = data
        self.details['platforms_present'] = not all(v is None for v in data)

    def get_details(self, id):
        data = json.loads(requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key={key}').text)
        genre = ""
        for g in data['genres']:
            genre += g['name'] + " | "
        if genre:
            genre = genre[:-3]

        self.details = {
            'title': data['title'],
            'rating': data['vote_average'],
            'no_of_users_rated': data['vote_count'],
            'status': "Yes" if data['status'] == "Released" else "No",
            'date': data['release_date'] if data['release_date'] else "0000",
            'summary': data['overview'],
            'genres': genre,
        }

    def get_images(self, id):
        image_data = json.loads(requests.get(f'https://api.themoviedb.org/3/movie/{id}/images?api_key={key}').text)
        self.details['images'] = []
        for i, image in enumerate(image_data['posters']):
            if i >= 2:
                break
            self.details['images'].append({
                'image': image_url + str(image['file_path']),
                'vertical': True
            })
        for i, image in enumerate(image_data['backdrops']):
            if len(self.details['images']) >= 5:
                break
            self.details['images'].append({
                'image': image_url + str(image['file_path']),
                'vertical': False
            })

    def get_credits(self, id):
        data = json.loads(requests.get(f'https://api.themoviedb.org/3/movie/{id}/credits?api_key={key}').text)
        cast, crew = [], []
        for cast_ in data['cast']:
            cast.append({
                'name': cast_['name'],
                'character': cast_['character'],
                'image': (image_url + str(cast_['profile_path'])) if cast_['profile_path'] else "/static/images/default_profile.jpeg"
            })
        for crew_ in data['crew']:
            crew.append({
                'name': crew_['name'],
                'job': crew_['job'],
                'image': (image_url + str(crew_['profile_path'])) if crew_['profile_path'] else "/static/images/default_profile.jpeg"
            })
        self.details['cast'] = cast
        self.details['crew'] = crew

    def get_reviews(self, id):
        data = json.loads(requests.get(f'https://api.themoviedb.org/3/movie/{id}/reviews?api_key={key}').text)
        reviews = []
        for review in enumerate(data['results']):
            reviews.append({
                'user': review[1]['author'],
                'review': review[1]['content'],
            })
        self.details['reviews'] = reviews

    def get_recommendations(self, id):
        data = json.loads(requests.get(f'https://api.themoviedb.org/3/movie/{id}/recommendations?api_key={key}').text)['results']
        self.details['recommendations'] = []
        for d in data:
            if d['backdrop_path'] or d['poster_path']:
                self.details['recommendations'].append({
                    'id': d['id'],
                    'name': d['title'],
                    'poster': image_url + (d['backdrop_path'] if d['backdrop_path'] else d['poster_path']),
                    'type': 'movie',
                    'date': d['release_date'][:4]
                })
        if not self.details['recommendations']:
            data = json.loads(requests.get(f'https://api.themoviedb.org/3/movie/{id}/similar?api_key={key}').text)['results']
            for d in data:
                if d['backdrop_path'] or d['poster_path']:
                    self.details['recommendations'].append({
                        'id': d['id'],
                        'name': d['title'],
                        'poster': image_url + (d['backdrop_path'] if d['backdrop_path'] else d['poster_path']),
                        'type': 'movie',
                        'date': d['release_date'][:4]
                    })

    def save_data(self, id):
        data = MovieData(id=id, title=self.details['title'], rating=self.details['rating'],
                         no_of_users_rated=self.details['no_of_users_rated'], status=self.details['status'],
                         date=self.details['date'], summary=self.details['summary'], genres=self.details['genres'],
                         images=self.details['images'], cast=self.details['cast'], crew=self.details['crew'],
                         reviews=self.details['reviews'], recommendations=self.details['recommendations'],
                         platforms=self.details['platforms'], platforms_present=self.details['platforms_present'])
        data.save()

    def get_data(self, id):
        data = MovieData.objects.all()
        for d in data:
            if d.id == id:
                self.details['title'] = d.title
                self.details['rating'] = d.rating
                self.details['no_of_users_rated'] = d.no_of_users_rated
                self.details['status'] = d.status
                self.details['date'] = d.date
                self.details['summary'] = d.summary
                self.details['genres'] = d.genres
                self.details['images'] = d.images
                self.details['cast'] = d.cast
                self.details['crew'] = d.crew
                self.details['reviews'] = d.reviews
                self.details['recommendations'] = d.recommendations
                self.details['platforms'] = d.platforms
                self.details['platforms_present'] = d.platforms_present


class ShowDetails:
    def __init__(self, id):
        self.details = {}
        self.get_data(id)

    def get_shows(self, id, year):
        name = self.details['title']
        data = [airtel_show(name, id, year), alt_balaji_show(name, id, year), eros_now_show(name, id, year),
                idea_show(name, id, year), jio_show(name, id, year), mx_player_show(name, id, year),
                vodafone_show(name, id, year), zee5_show(name, id, year), sony_liv_show(name, id, year),
                hotstar_show(name, id, year)]
        self.details['platforms'] = data
        self.details['platforms_present'] = not all(v is None for v in data)

    def get_details(self, id):
        data = json.loads(requests.get(f'https://api.themoviedb.org/3/tv/{id}?api_key={key}').text)
        genre = ""
        for g in data['genres']:
            genre += g['name'] + " | "
        if genre:
            genre = genre[:-3]

        self.details = {
            'title': data['name'],
            'rating': data['vote_average'],
            'no_of_users_rated': data['vote_count'],
            'date': data['first_air_date'] if data['first_air_date'] else "0000",
            'summary': data['overview'],
            'genres': genre,
            'seasons': data['number_of_seasons'],
        }

    def get_images(self, id):
        image_data = json.loads(requests.get(f'https://api.themoviedb.org/3/tv/{id}/images?api_key={key}').text)
        self.details['images'] = []
        for i, image in enumerate(image_data['posters']):
            if i >= 2:
                break
            self.details['images'].append({
                'image': image_url + str(image['file_path']),
                'vertical': True
            })
        for i, image in enumerate(image_data['backdrops']):
            if len(self.details['images']) >= 5:
                break
            self.details['images'].append({
                'image': image_url + str(image['file_path']),
                'vertical': False
            })

    def get_credits(self, id):
        data = json.loads(requests.get(f'https://api.themoviedb.org/3/tv/{id}/credits?api_key={key}').text)
        cast, crew = [], []
        for cast_ in data['cast']:
            cast.append({
                'name': cast_['name'],
                'character': cast_['character'],
                'image': (image_url + str(cast_['profile_path'])) if cast_['profile_path'] else "/static/images/default_profile.jpeg"
            })
        for crew_ in data['crew']:
            crew.append({
                'name': crew_['name'],
                'job': crew_['job'],
                'image': (image_url + str(crew_['profile_path'])) if crew_['profile_path'] else "/static/images/default_profile.jpeg"
            })
        self.details['cast'] = cast
        self.details['crew'] = crew

    def get_reviews(self, id):
        data = json.loads(requests.get(f'https://api.themoviedb.org/3/tv/{id}/reviews?api_key={key}').text)
        reviews = []
        for review in enumerate(data['results']):
            reviews.append({
                'user': review[1]['author'],
                'review': review[1]['content'],
            })
        self.details['reviews'] = reviews

    def get_recommendations(self, id):
        data = json.loads(requests.get(f'https://api.themoviedb.org/3/tv/{id}/recommendations?api_key={key}').text)['results']
        self.details['recommendations'] = []
        for d in data:
            if d['backdrop_path'] or d['poster_path']:
                self.details['recommendations'].append({
                    'id': d['id'],
                    'name': d['name'],
                    'poster': image_url + (d['backdrop_path'] if d['backdrop_path'] else d['poster_path']),
                    'type': "show",
                    'date': d['first_air_date'][:4]
                })
        if not self.details['recommendations']:
            data = json.loads(requests.get(f'https://api.themoviedb.org/3/tv/{id}/similar?api_key={key}').text)['results']
            for d in data:
                if d['backdrop_path'] or d['poster_path']:
                    self.details['recommendations'].append({
                        'id': d['id'],
                        'name': d['name'],
                        'poster': image_url + (d['backdrop_path'] if d['backdrop_path'] else d['poster_path']),
                        'type': "show",
                        'date': d['first_air_date'][:4]
                    })

    def save_data(self, id):
        data = SeriesData(id=id, title=self.details['title'], rating=self.details['rating'],
                         no_of_users_rated=self.details['no_of_users_rated'], date=self.details['date'],
                         summary=self.details['summary'], genres=self.details['genres'], seasons=self.details['seasons'],
                         images=self.details['images'], cast=self.details['cast'], crew=self.details['crew'],
                         reviews=self.details['reviews'], recommendations=self.details['recommendations'],
                         platforms=self.details['platforms'], platforms_present=self.details['platforms_present'])
        data.save()

    def get_data(self, id):
        data = SeriesData.objects.all()
        for d in data:
            if d.id == id:
                self.details['title'] = d.title
                self.details['rating'] = d.rating
                self.details['no_of_users_rated'] = d.no_of_users_rated
                self.details['date'] = d.date
                self.details['summary'] = d.summary
                self.details['genres'] = d.genres
                self.details['seasons'] = d.seasons
                self.details['images'] = d.images
                self.details['cast'] = d.cast
                self.details['crew'] = d.crew
                self.details['reviews'] = d.reviews
                self.details['recommendations'] = d.recommendations
                self.details['platforms'] = d.platforms
                self.details['platforms_present'] = d.platforms_present


def movieDetails(request):
    id = request.GET['id']
    year = request.GET['year']
    type_ = request.GET['type']
    if type_ == "movie":
        mv = MovieDetails(id)
        if not mv.details:
            mv.get_details(id)
            mv.get_images(id)
            mv.get_credits(id)
            mv.get_reviews(id)
            mv.get_recommendations(id)
            mv.get_movies(id, year)
            mv.save_data(id)
        return render(request, 'details.html', context=mv.details)
    else:
        sh = ShowDetails(id)
        if not sh.details:
            sh.get_details(id)
            sh.get_images(id)
            sh.get_credits(id)
            sh.get_reviews(id)
            sh.get_recommendations(id)
            sh.get_shows(id, year)
            sh.save_data(id)
        return render(request, 'details.html', context=sh.details)


if __name__ == "__main__":
    # get_movies(12345)
    mv = MovieDetails(24428)
    mv.get_recommendations(24428)
