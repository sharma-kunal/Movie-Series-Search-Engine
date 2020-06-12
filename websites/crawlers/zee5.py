import requests
from .helper import condition

url = "https://gwapi.zee5.com/content/getContent/search?q={}&start=0&limit=24&asset_type=0,6,1&country=IN&\
        languages=en,hi,pa&translation=en&version=3&page=1"
link = "https://www.zee5.com/{}/details/{}/{}"


def zee5_movie(name, id, year):
    def find_movie(data, name, id, year):
        result = None
        try:
            for movies in data:
                if condition(title=movies['title'].lower(), name=name.lower()):
                    if 'release_date' in movies:
                        if year == movies['release_date'][:4]:
                            return {
                                'id': id,
                                'name': movies['title'],
                                'source': 'zee5',
                                'link': link.format("movies", movies['title'], movies['id']),
                                'logo': "/static/images/logos/zee5.png"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': movies['title'],
                            'source': 'zee5',
                            'link': link.format("movies", movies['title'], movies['id']),
                            'logo': "/static/images/logos/zee5.png"
                        }
            return result
        except Exception:
            return None

    print("zee 5")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(url.format(name))
            break
        except Exception:
            counter += 1
    if response and response.status_code == 200:
        data = response.json()
        try:
            return find_movie(data['movies'], name, id, year)
        except KeyError:
            return None


def zee5_show(name, id, year):
    def find_show(data, name, id, year):
        try:
            result = None
            for d in data:
                if condition(title=d['title'].lower(), name=name.lower()):
                    if 'release_date' in d:
                        if year == d['release_date'][:4]:
                            return {
                                'id': id,
                                'name': name,
                                'source': 'zee5',
                                'link': link.format("movies", d['title'], d['id']),
                                'logo': "/static/images/logos/zee5.png"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': name,
                            'source': 'zee5',
                            'link': link.format("movies", d['title'], d['id']),
                            'logo': "/static/images/logos/zee5.png"
                        }
            return result
        except Exception:
            return None

    print("zee 5")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(url.format(name))
            break
        except Exception:
            counter += 1
    if response and response.status_code == 200:
        data = response.json()
        try:
            return find_show(data['tvshows'], name, id, year)
        except KeyError:
            return None


if __name__ == "__main__":
    print(zee5_movie("chintu ka birthday", 12345, "2020"))
    print(zee5_show("baarish", 12345, "2020"))
