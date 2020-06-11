import requests
from .helper import condition

endpoint = "https://search.airtel.tv/app/v3/search/atv/query?appId=WEB&bn=15&count=30&dt=BROWSER&ln=hi&offSet=0&os=WEBOS&q={}"
link = "https://www.airtelxstream.in/{}/{}/{}"


def airtel_movie(name, id, year):
    def find_movie(data, name, id, year):
        try:
            result = None

            # Searching Algorithm
            # 1). If json object does not have release date, then search further
            # 2). If json object has release date
            # 2 (a). If release date and title matches, then return the result
            # 2 (b). If release date does not match, then search further, but make the flag = False,
            #        which would tell that we dont need to update the result in the elif condition (because release
            #        date) is present

            for d in data:
                if (d['programType'] == "MOVIE") and condition(title=d['title'].lower(), name=name.lower()):
                    if 'releaseYear' in d:
                        if year == d['releaseYear']:
                            return {
                                'id': id,
                                'name': d['title'],
                                'source': "airtel",
                                'link': link.format("movies", d['title'], d['id']),
                                'logo': "/static/images/logos/airtel.jpeg"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': d['title'],
                            'source': "airtel",
                            'link': link.format("movies", d['title'], d['id']),
                            'logo': "/static/images/logos/airtel.jpeg"
                        }
            return result
        except Exception:
            return None

    print("airtel")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(endpoint.format(name))
            break
        except Exception:
            counter += 1
    if response and response.status_code == 200:
        try:
            data = response.json()['categories']
            for d in data:
                if d['type'] == "MOVIE":
                    return find_movie(d['contentResponseList'], name, id, year)
        except Exception:
            return None
    return None


def airtel_show(name, id, year):
    def find_show(data, name, id, year):
        result = None
        try:
            for d in data:
                if condition(title=d['title'].lower(), name=name.lower()):
                    if 'releaseYear' in d:
                        if year == d['releaseYear']:
                            return {
                                'id': id,
                                'name': d['title'],
                                'source': "airtel",
                                'link': link.format("tv-shows", d['title'], d['id']),
                                'logo': "/static/images/logos/airtel.jpeg"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': d['title'],
                            'source': "airtel",
                            'link': link.format("tv-shows", d['title'], d['id']),
                            'logo': "/static/images/logos/airtel.jpeg"
                        }
            return result
        except Exception:
            return None

    print("airtel")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(endpoint.format(name))
            break
        except Exception:
            counter += 1
    if response and response.status_code == 200:
        try:
            data = response.json()['categories']
            for d in data:
                if d['type'] == "TVSHOW":
                    return find_show(d['contentResponseList'], name, id, year)
        except Exception:
            return None
    return None


if __name__ == "__main__":
    print(airtel_movie("queen", 12345, "2013"))
    print(airtel_show("mismatch", 12345, "2018"))