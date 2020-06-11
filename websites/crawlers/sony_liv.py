import requests
from .helper import condition

endpoint = "https://www.sonyliv.com/api/v4/vod/videos/search?search={}&deviceDetails=%7B%22mfg%22:%22WEB%22,%22os%22:%22others%22,%22osVer%22:%22XXX%22,%22model%22:%22WEB%22,%22deviceId%22:%22cf51a79c-69b8-45e8-b070-2e0356f25a34%22%7D&isSearchable=true&pageNumber=1&pageSize=12"
movie_link = "https://www.sonyliv.com/details/{}/{}/{}"


def sony_liv_movie(name, id, year):
    def find_movie(data, name, id, year):
        try:
            for d in data:
                if condition(title=d['title'].lower(), name=name.lower()) and d['category'] == "Movie":
                    return {
                        'id': id,
                        'name': d['title'],
                        'source': 'sony liv',
                        'link': movie_link.format("full movie", d['referenceId'], d['title']),
                        'logo': "/static/images/logos/sony_liv.jpeg"
                    }
            return None
        except Exception:
            return None

    print("sony liv")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(endpoint.format(name))
            break
        except Exception:
            counter += 1
    if response and response.status_code == 200:
        data = response.json()
        return find_movie(data, name, id, year)
    return None


def sony_liv_show(name, id, year):
    def find_show(data, name, id, year):
        try:
            for d in data:
                if condition(title=d['title'].lower(), name=name.lower()) and d['responseItemType'] == "show":
                    return {
                        'id': id,
                        'name': d['title'],
                        'source': 'sony liv',
                        'link': movie_link.format("show", d['referenceId'], d['title']),
                        'logo': "/static/images/logos/sony_liv.jpeg"
                    }
            return None
        except Exception:
            return None

    print("sony liv")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(endpoint.format(name))
            break
        except Exception:
            counter += 1
    if response and response.status_code == 200:
        data = response.json()
        return find_show(data, name, id, year)
    return None


if __name__ == "__main__":
    print(sony_liv_movie("queen", 12345, "2017"))
    print(sony_liv_show("bar code", 12345, "2019"))
