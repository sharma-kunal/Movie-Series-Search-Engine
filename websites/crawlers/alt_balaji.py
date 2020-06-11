import requests
from .helper import condition

endpoint = "https://api.cloud.altbalaji.com/media/videos?query={}&tags[]=&limit=50&offset=0&domain=IN"
url = "https://altbalaji.com/{}/{}"
name_link = "https://api.cloud.altbalaji.com/media/series/{}?domain=IN"


def alt_balaji_movie(name, id, year):
    def get_movie(data, name, id, year):
        result = None
        try:
            for d in data:
                if d['tags'][0] == "type-movie" and condition(title=d['titles']['default'].lower(), name=name.lower()):
                    if ('dates' in d) and ('published' in d['dates']):
                        if year == d['dates']['published'][:4]:
                            return {
                                'id': id,
                                'name': name,
                                'source': 'alt_balaji',
                                'link': url.format("media", d['id']),
                                'logo': "/static/images/logos/alt_balaji.png"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': name,
                            'source': 'alt_balaji',
                            'link': url.format("media", d['id']),
                            'logo': "/static/images/logos/alt_balaji.png"
                        }
            return result
        except Exception:
            return None

    print("alt balaji")
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
            data = response.json()['media']
            return get_movie(data, name, id, year)
        return None
    except Exception:
        return None


def alt_balaji_show(name, id, year):
    def get_show(data, name, id, year):
        result = None
        try:
            for d in data:
                if d['tags'][0] == "type-episode" and condition(title=d['tags'][5], name=name.lower().replace(" ", "-")):
                    if ('dates' in d) and ('published' in d['dates']):
                        if year == d['dates']['published'][:4]:
                            return {
                                'id': id,
                                'name': name,
                                'source': "alt balaji",
                                'link': url.format("show", name) + "/" + d['_links']['series']['href'].split('/')[-1],
                                'logo': "/static/images/logos/alt_balaji.png"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': name,
                            'source': "alt balaji",
                            'link': url.format("show", name) + "/" + d['_links']['series']['href'].split('/')[-1],
                            'logo': "/static/images/logos/alt_balaji.png"
                        }
            return result
        except Exception:
            return None

    print("alt balaji")
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
            data = response.json()['media']
            return get_show(data, name, id, year)
        return None
    except Exception:
        return None


if __name__ == "__main__":
    print(alt_balaji_movie("Once Upon A Time In Mumbaai", 12345, "2010"))
    print(alt_balaji_show("Class Of 2020", 12345, "2020"))