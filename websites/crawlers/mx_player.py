import requests
from .helper import condition

endpoint = "https://api.mxplay.com/v1/web/search/result?query={}&userid=0cc7582c-09de-4f53-bfda-6f6564372de3&platform=com.mxplay.desktop&content-languages=hi,en"

url = "https://www.mxplayer.in"


def mx_player_movie(name, id, year):
    def get_movie(data, name, id, year):
        result = None
        try:
            for d in data:
                if condition(title=d['title'].lower(), name=name.lower()):
                    if 'releaseDate' in d:
                        if year == d['releaseDate'][:4]:
                            return {
                                'id': id,
                                'name': d['title'],
                                'source': "mx_player",
                                'link': url + d['shareUrl'],
                                'logo': "/static/images/logos/mx_player.jpg"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': d['title'],
                            'source': "mx_player",
                            'link': url + d['shareUrl'],
                            'logo': "/static/images/logos/mx_player.jpg"
                        }
            return result
        except Exception:
            return None

    print("mx player")
    response = None
    counter = 0
    while counter < 3:
        try:
            response = requests.get(endpoint.format(name))
            break
        except Exception:
            counter += 1
    if response and response.status_code == 200:
        data = response.json()['sections']
        for d in data:
            if d['id'] == "movie":
                return get_movie(d['items'], name, id, year)
    return None


def mx_player_show(name, id, year):
    def get_show(data, name, id, year):
        result = None
        try:
            for d in data:
                if condition(title=d['title'].lower(), name=name.lower()):
                    if 'releaseDate' in d:
                        if year == d['releaseDate'][:4]:
                            return {
                                'id': id,
                                'name': name,
                                'source': "mx_player",
                                'link': url + d['shareUrl'],
                                'logo': "/static/images/logos/mx_player.jpg"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': name,
                            'source': "mx_player",
                            'link': url + d['shareUrl'],
                            'logo': "/static/images/logos/mx_player.jpg"
                        }
            return result
        except Exception:
            return None

    print("mx player")
    response = None
    counter = 0
    while counter < 3:
        try:
            response = requests.get(endpoint.format(name))
            break
        except Exception:
            counter += 1
    if response and response.status_code == 200:
        data = response.json()['sections']
        for d in data:
            if d['id'] == "shows":
                return get_show(d['items'], name, id, year)
    return None


if __name__ == "__main__":
    print(mx_player_movie("Ugly", 12345, "2012"))
    print(mx_player_show("mastram", 12345, "2020"))