import requests
import json

TMDB_API_KEY = '5409f4c3910231c41d381e6b518db90a'
# https://api.themoviedb.org/3/movie/popular?api_key=db810f1ce85d6d911d7c5d0b9f259284&language=ko-KR&page=1
# https://api.themoviedb.org/3/movie/436270/videos?api_key=db810f1ce85d6d911d7c5d0b9f259284language=en-US
def get_movie_datas():
    total_data = []

    for i in range(1, 10):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()
        for movie in movies["results"]:
            movie_id = movie["id"]
            # print(movie_id)
            request_url1 = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={TMDB_API_KEY}&language=en-US"
            trailers = requests.get(request_url1).json()
            # print(trailers)
            # print(trailers["results"])
            url = ""
            if movie.get('release_date', ''):
                for result in trailers["results"]:
                    if result["type"] == 'Trailer':
                        url = result["key"]
                    elif result["type"] == "Teaser":
                        url = result["key"]
                
                
                fields = {
                    # 'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'youtube_url': url,

                    
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)




get_movie_datas()


'''
movies/fixtures/ 만들고 

python init2.py 

python manage.py migrate

python manage.py loaddata genre_data.json movie_data.json

'''