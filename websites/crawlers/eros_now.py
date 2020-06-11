import requests, json
from .helper import condition


endpoint = "https://pwaproxy.erosnow.com/api/v2/search?q={}&start=0&rows=10&optimized=true&country=IN"
url = "https://erosnow.com/{}/watch/{}/{}"


def eros_now_movie(name, id, year):
    def find_movie(data, name, id, year):
        result = None
        try:
            for movie in data:
                if condition(title=movie['title'].lower(), name=name.lower()):
                    if 'release_year' in movie:
                        if year == movie['release_year']:
                            return {
                                'id': id,
                                'name': movie['title'],
                                'source': "eros_now",
                                'link': url.format(movie['asset_type'].lower(), movie['asset_id'], movie['title']),
                                'logo': "/static/images/logos/eros_now.png"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': movie['title'],
                            'source': "eros_now",
                            'link': url.format(movie['asset_type'].lower(), movie['asset_id'], movie['title']),
                            'logo': "/static/images/logos/eros_now.png"
                        }
            return result
        except KeyError:
            return None

    print("eros now")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(endpoint.format(name))
            break
        except Exception:
            counter += 1
    try:
        if response and response.status_code == 200:
            data = json.loads(response.text)
            # if data.get("movies", None) and data.get("originals", None):
            #     return find_movie(data['movies']['rows'] + data['originals']['rows'], name, id, year)
            if data.get("movies", None):
                return find_movie(data['movies']['rows'], name, id, year)
            # elif data.get("originals", None):
            #     return find_movie(data['originals']['rows'], name, id, year)
        return None
    except Exception:
        return None


def eros_now_show(name, id, year):
    def find_show(data, name, id, year):
        try:
            for d in data:
                if condition(title=d['title'].lower(), name=name.lower()):
                    return {
                        'id': id,
                        'name': name,
                        'source': "eros now",
                        'link': url.format(d['asset_type'].lower(), d['asset_id'], d['title']),
                        'logo': "/static/images/logos/eros_now.png"
                    }
            return None
        except Exception:
            return None

    print("eros now")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(endpoint.format(name))
            break
        except Exception:
            counter += 1
    try:
        if response and response.status_code == 200:
            data = json.loads(response.text)
            if data.get("tvshow", None) and data.get("originals", None):
                return find_show(data['tvshow']['rows'] + data['originals']['rows'], name, id, year)
            elif data.get("tvshow", None):
                return find_show(data['tvshow']['rows'], name, id, year)
            elif data.get("originals", None):
                return find_show(data['originals']['rows'], name, id, year)
        return None
    except Exception:
        return None


if __name__ == "__main__":
    print(eros_now_movie("Housefull 3", 12345, "2016"))
    print(eros_now_show("metro park", 12345, "2019"))