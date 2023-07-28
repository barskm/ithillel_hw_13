from film_player.media_player import Player
from film_player.films_worker import Film

import os
import string

# ----- Крок 4 -----
# movie = Player(name->required, link-required)
movie = Player('test','https://google.com')
movie.play()

# ----- Крок 5 -----
if not os.path.isdir('film_storage'):
    os.mkdir('film_storage')
else:
    print('Folder -film_storage- alredy exist')

for count in range(26):
    dir_path = "film_storage/" + string.ascii_uppercase[count]
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    else:
        print(f'Folder -{dir_path}- alredy exist.')

# ----- Крок 7 -----
# newFilm = Film(film_name->required, film_year->required, film_descr->optional, film_writer->optional, storge_address->optional
film_name = 'test'
film_year = 1999
newFilm = Film(film_name,film_year)
newFilm.get_film_address(film_name, film_year)
print(newFilm.storage_address)