import json
from vars import ganres, films_data
import os
import csv

dict1 = json.loads(ganres)
for i in dict1['results']:

  # ----- Create Directories -----
  os.mkdir(i['genre'])

  # ----- Create empty csv files -----
  csv_header = {'title': None, 'year': None, 'rating': None, 'type': None, 'ganres': None}
  csv_f_path = i['genre'] + '/' + 'csv_genre.csv'
  with open(csv_f_path, 'w') as file:
    csv_file = csv.writer(file)
    csv_file.writerow(csv_header)

#----- Generate data & save to file
for film in films_data:
  list_of_genres = ''
  #----- Create dict() with film data to write -----
  film_data_to_write = {
    'title': film['title'],
    'year': film['year'],
    'rating': film['rating'],
    'type': film['type']
  }
  #----- Cicle for genres -----
  for genre in film['gen']:
    list_of_genres += genre['genre'] + ';'
  film_data_to_write['ganre'] = list_of_genres

  # ----- Cicle for generate files -----
  for genre in film['gen']:
    csv_f_path = genre['genre'] + '/' + 'csv_genre.csv'
    with open(csv_f_path, 'a', encoding="utf-8") as file:
      reader = csv.DictWriter(file,fieldnames = film_data_to_write.keys())
      reader.writerow(film_data_to_write)
