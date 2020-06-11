import requests
from .helper import condition


movies_endpoint = "https://api2.ideamoviesandtv.in/content/v7/search/?fields=generalInfo,contents&level=&query={}&startIndex=1&count=10&orderBy=releaseDate&orderMode=1&publishingHouseId=1,5,10,43,51,52,53,55,57,58,61,63,66,67,68,69,70,71,81,82,83,85,86,100&type=movie"
link = "https://www.ideamoviesandtv.in/{}/detail/{}/{}"
show_endpoint = "https://api2.ideamoviesandtv.in/content/v7/search/?fields=generalInfo,contents&level=&query={}&startIndex=1&count=10&orderBy=releaseDate&orderMode=1&publishingHouseId=1,5,10,43,51,52,53,55,57,58,61,63,66,67,68,69,70,71,81,82,83,85,86,100&type=tvshow%2Ctvseries"


def idea_movie(name, id, year):
    print("Idea")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(movies_endpoint.format(name))
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
                                'source': 'idea',
                                'link': link.format("movies", str(d['generalInfo']['_id']), d['generalInfo']['title']),
                                'logo': "/static/images/logos/idea.png"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': d['generalInfo']['title'],
                            'source': 'idea',
                            'link': link.format("movies", str(d['generalInfo']['_id']), d['generalInfo']['title']),
                            'logo': "/static/images/logos/idea.png"
                        }
            return result
        except Exception:
            return None


def idea_show(name, id, year):
    print("Idea")
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
                                'source': 'idea',
                                'link': link.format("tvseries", str(d['generalInfo']['_id']), d['generalInfo']['title']),
                                'logo': "/static/images/logos/idea.png"
                            }
                        else:
                            result = None
                    elif result is None:
                        result = {
                            'id': id,
                            'name': d['generalInfo']['title'],
                            'source': 'idea',
                            'link': link.format("tvseries", str(d['generalInfo']['_id']), d['generalInfo']['title']),
                            'logo': "/static/images/logos/idea.png"
                        }
            return result
        except Exception:
            return None


if __name__ == "__main__":
    print(idea_movie("piku", 12345, "2015"))
    print(idea_show("once upon a crime", 12345, "2020"))