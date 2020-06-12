import requests
from .helper import condition

headers = {
    'Host': 'api.hotstar.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.hotstar.com/in',
    'x-country-code': 'IN',
    'x-platform-code': 'PCTV',
    'x-client-code': 'LR',
    'hotstarauth': 'st=1591731250~exp=1591737250~acl=/*~hmac=30e290968fac98e02d39b937ec556c42d1692d6493d0ae29e49bcb1723829e23',
}

endpoint = "https://api.hotstar.com/s/v1/scout?q={}&perPage=50"
link = "https://www.hotstar.com/in"


def hotstar_movie(name, id, year):
    def find_movie(data, name, id, year):
        result = None
        try:
            for d in data:
                if (d['entityType'] == "MOVIE") and condition(title=d['title'].lower(), name=name.lower()):
                    if 'year' in d:
                        if year == str(d['year']):
                            return {
                                'id': id,
                                'name': d['title'],
                                'source': "hotstar",
                                "link": link + f"/movies/{d['title']}/{d['contentId']}",
                                'logo': "/static/images/logos/hotstar.png"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': d['title'],
                            'source': "hotstar",
                            "link": link + f"/movies/{d['title']}/{d['contentId']}",
                            'logo': "/static/images/logos/hotstar.png"
                        }
            return result
        except Exception:
            return None

    print("hotstar")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(endpoint.format(name), headers=headers)
            break
        except Exception:
            counter += 1
    try:
        if response and response.status_code == 200:
            data = response.json()['body']['results']['items']
            return find_movie(data, name, id, year)
    except Exception:
        return None


def hotstar_show(name, id, year):
    def find_show(data, name, id, year):
        try:
            for d in data:
                if (d['entityType'] == "SHOW") and condition(title=d['title'].lower(), name=name.lower()):
                    return {
                        'id': id,
                        'name': d['title'],
                        'source': "hotstar",
                        "link": link + f"/tv/{d['title']}/{d['contentId']}",
                        'logo': "/static/images/logos/hotstar.png"
                    }
            return None
        except Exception:
            return None

    print("hotstar")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(endpoint.format(name), headers=headers)
            break
        except Exception:
            counter += 1
    try:
        if response and response.status_code == 200:
            data = response.json()['body']['results']['items']
            return find_show(data, name, id, year)
    except Exception:
        return None


if __name__ == "__main__":
    print(hotstar_movie("John Wick: Chapter 3 - Parabellum", 12345, '2015'))
    print(hotstar_show("avengers assemble", 12345, "2020"))
