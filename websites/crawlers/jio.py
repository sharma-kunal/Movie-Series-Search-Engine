import requests
from .helper import condition

link = "https://www.jiocinema.com/watch/{}/{}/{}/{}/{}/0/0"
endpoint = "http://prod.media.jio.com/apis/common/v3.1/search/search"


def jio_movie(name, id, year):
    def find_movie(data, name, id, year):
        result = None
        try:
            for movie in data['items']:
                if condition(title=movie['name'].lower(), name=name.lower()):
                    if 'subtitle' in movie:
                        if year == movie['subtitle'][-4:]:
                            return {
                                'id': id,
                                'name': movie['name'],
                                'source': "jio",
                                'link': link.format("movies", movie['name'], "0", "0", movie['id']),
                                'logo': "/static/images/logos/jio.png"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': movie['name'],
                            'source': "jio",
                            'link': link.format("movies", movie['name'], "0", "0", movie['id']),
                            'logo': "/static/images/logos/jio.png"
                        }
            return result
        except KeyError:
            return None

    print("jio")
    data = {
        "q": name
    }
    try:
        counter = 0
        response = None
        while counter < 3:
            try:
                response = requests.post(endpoint, data=data)
                break
            except Exception:
                counter += 1
        if response and response.status_code == 200:
            data = response.json()
            try:
                for d in data['data']['items']:
                    if d['name'] == "Movies":
                        return find_movie(d, name, id, year)
            except KeyError:
                return None
        else:
            return None
    except Exception:
        return None


def jio_show(name, id, year):
    def find_show(data, name, id, year):
        try:
            for movie in data['items']:
                if condition(title=movie['name'].lower(), name=name.lower()):
                    return {
                        'id': id,
                        'name': movie['name'],
                        'source': "jio",
                        'link': link.format("tv", movie['name'], "1", "1", movie['id']),
                        'logo': "/static/images/logos/jio.png"
                    }
            return None
        except KeyError:
            return None

    print("jio")
    data = {
        "q": name
    }
    try:
        counter = 0
        response = None
        while counter < 3:
            try:
                response = requests.post(endpoint, data=data)
                break
            except Exception:
                counter += 1
        if response and response.status_code == 200:
            data = response.json()
            try:
                for d in data['data']['items']:
                    if d['name'] == "TV Shows":
                        return find_show(d, name, id, year)
            except KeyError:
                return None
        else:
            return None
    except Exception:
        return None


if __name__ == "__main__":
    print(jio_movie("Sarkar", 12345, "2017"))
    print(jio_show("Once Upon A Crime", 12345, "2000"))