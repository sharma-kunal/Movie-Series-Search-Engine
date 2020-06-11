# Movie/Series Search Engine

This is a Movies/Series Search Engine made using Django. It searches for the Movie/Show on 10 Streaming Services. The Services are

* Hotstar
* Airtel Xstream
* Idea Movies And TV
* MX Player
* Jio Cinema
* Vodafone Play
* Eros Now
* Zee5
* Alt Balaji
* Sony LIV

![Demo](https://github.com/sharma-kunal/Movie-Series-Search-Engine/blob/master/readmeData/johnwick3.gif)


**NOTE**
Currently some major services like Netflix and Amazon Prime Video are not included, but I am working on adding these services in the next version.

## Installation & Running

1. Get the API-KEY from the [TMDB Website](https://developers.themoviedb.org/3/getting-started/introduction).

2. Copy the key and paste it in the 'api-keys.txt' file in the place of `<your-api-key>`.

![Api KEY](https://github.com/sharma-kunal/Movie-Series-Search-Engine/blob/master/readmeData/apiKey.png)

3. You need to run the server on you machine, so for doing that, just go to the folder with `requirements.txt` file and run the command

```
pip install -r requirements.txt
```

4. Now run the server using the command, (please make sure you are in the directory where `manage.py` is present)

```
python manage.py runserver 127.0.0.1:8090
```

**NOTE**
I have made the server to run on the port 8090, if you want to change the port, you also need to change the port in the file `client/index.js` in function `search` on line 34.

![Port Image](https://github.com/sharma-kunal/Movie-Series-Search-Engine/blob/master/readmeData/port.png)

5. Now just run the file `client/index.html` and the project is up and running.

If any problem occurs, please let me know.


## Working

Currently there are lots of files in the project, which are not being used currently, but may be used in the future. So to clear any confusions, these are the `currently being used files` with their uses.

* `client` (Search Bar to search Movies/Show)
  * `index.html` (Main HTML File)
  * `index.css` (Styling File for index.html)
  * `index.js` (Javascript file for index.html)
* `finder` (Settings and URL's for the project)
* `scraper` (All the views, api, serializers and more)
  * `__init__.py`
  * `api.py` (REST API for handling AJAX requests from the search bar)
  * `serializers.py` (Serializers for the API)
  * `views.py` (All the views, the html for the details page)
* `static` (All the staic files, i.e css, js)
  * `css` (CSS files for the project)
  * `js` (JavaScript files for the project)
  * `images` (Images being used in the project)
* `templates` (HTML files for the project)
  * `details.html` (HTML File for showing the results)
* `websites` (All the crawlers to fetch data from the websites)
  * `crwalers` (Currently used crawlers are in this directory)
    * `airtel.py` (Crawler for Airtel XStream TV)
    * `alt_balaji.py` (Crawler for Alt Balaji)
    * `eros_now.py` (Crawler for Eros Now)
    * `hotstar.py` (Crawler for Hotstar)
    * `idea.py` (Crawler for Idea Movies and TV)
    * `jio.py` (Crawler for Jio Cinema)
    * `mx_player.py` (Crawler for MX Player)
    * `sony_liv.py` (Crawler for Sony LIV)
    * `vodafone.py` (Crawler for Vodafone Play)
    * `ze5e.py` (Crawler for ZEE5)

---
**NOTE** There are many other files in the project, but they are not currently being used. So please ignore them.


## Further Improvements

Currently the project is in development phase as there are many improvements that need to be done and many more functionalities that need to be added to the project. Some are

* Adding more Streaming Services like Netflix and Amazon Prime Videos
* Hosting the server and making proper UI for the app.

If you have any doubts regarding the project, feel free to message me.
If you want to contribute to the project, feel free to do so.

Happy Coding :)
