import requests
from .helper import condition

endpoint = "https://api.vodafoneplay.in/content/v7/search/?fields=generalInfo,contents&level=&query={}&\
        startIndex=1&count=10&orderBy=releaseDate&orderMode=1&publishingHouseId=1,5,10,43,51,52,\
        53,55,56,57,58,59,61,63,65,66,67,69,71,80,81,82,83,85,86,100&type=movie"

show_endpoint = "https://api.vodafoneplay.in/content/v7/search/?fields=generalInfo,contents&level=&query={}&\
        startIndex=1&count=10&orderBy=releaseDate&orderMode=1&publishingHouseId=1,5,10,43,51,52,\
        53,55,56,57,58,59,61,63,65,66,67,69,71,80,81,82,83,85,86,100&type=tvshow%2Ctvseries"

movies_link = "https://www.vodafoneplay.in/movies/detail/{}/{}"


def vodafone_movie(name, id, year):
    print("Vodafone")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(endpoint.format(name))
            break
        except Exception:
            counter += 1
    if response and response.status_code == 200:
        result = None
        try:
            data = response.json()['results']
            for d in data:
                if condition(title=d['generalInfo']['title'].lower(), name=name.lower()):
                    if ('content' in d) and ('releaseDate' in d['content']):
                        if year == d['content']['releaseDate'][:4]:
                            return {
                                'id': id,
                                'name': d['generalInfo']['title'],
                                'source': 'vodafone',
                                'link': movies_link.format(str(d['generalInfo']['_id']), d['generalInfo']['title']),
                                'logo': "/static/images/logos/vodafone.jpg"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': d['generalInfo']['title'],
                            'source': 'vodafone',
                            'link': movies_link.format(str(d['generalInfo']['_id']), d['generalInfo']['title']),
                            'logo': "/static/images/logos/vodafone.jpg"
                        }
            return result
        except Exception as e:
            return None


def vodafone_show(name, id, year):
    print("Vodafone")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(show_endpoint.format(name))
            break
        except Exception:
            counter += 1
    if response and response.status_code == 200:
        result = None
        try:
            data = response.json()['results']
            for d in data:
                if condition(title=d['generalInfo']['title'].lower(), name=name.lower()):
                    if ('content' in d) and ('releaseDate' in d['content']):
                        if year == d['content']['releaseDate'][:4]:
                            return {
                                'id': id,
                                'name': d['generalInfo']['title'],
                                'source': 'vodafone',
                                'link': movies_link.format(str(d['generalInfo']['_id']), d['generalInfo']['title']),
                                'logo': "/static/images/logos/vodafone.jpg"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': d['generalInfo']['title'],
                            'source': 'vodafone',
                            'link': movies_link.format(str(d['generalInfo']['_id']), d['generalInfo']['title']),
                            'logo': "/static/images/logos/vodafone.jpg"
                        }
            return result
        except Exception as e:
            print(e)
            return None


if __name__ == "__main__":
    print(vodafone_movie("John Wick Chapter 2: Wick-vizzed", 12345, "2017"))
    print(vodafone_show("gandii baat", 12345, "2019"))