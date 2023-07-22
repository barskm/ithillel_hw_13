import os
import string
from pprint import pprint
from vars import films_awards, films_titles

os.mkdir("Harry Potter")

for dirs in films_titles["results"]:
    directory = "Harry Potter/"+ dirs["title"].replace(":", "")
    os.mkdir(directory)
    for count in range(26):
        os.mkdir(directory + "/" + string.ascii_uppercase[count])

films = films_awards
film_titles = films_titles['results']

films_list = []

for film_title in film_titles:
    movie_title = film_title['title'].replace(":", "")
    movie_awards = []
    for film in films:
        for result in film['results']:
            if result['movie']['imdb_id'] == film_title['imdb_id']:
                award_dict = {
                    'type': result['type'],
                    'award_name': result['award_name'],
                    'award': result['award']
                }
                movie_awards.append(award_dict)
    sorted_movie_awards = sorted(movie_awards, key=lambda x: x['award_name'])
    films_list.append({movie_title: sorted_movie_awards})


os.chdir("Harry Potter")

for stage1 in films_list:

  for st2_key, st2_value in stage1.items():

    for stage3 in st2_value:
      folder_film_name = st2_key
      award_name = stage3["award_name"]
      folder_award = stage3["award_name"][0]
      award_content = stage3["award"]

      file_link = folder_film_name + "/" + folder_award + "/" + award_name + ".txt"

      file = open(file_link, "w", encoding="utf-8")
      file.write(award_content)
      file.close()



