class Film:

    def __init__(self, film_name, film_year, film_descr='---', film_writer='---'):
        self.storage_address = None
        self.file_path = None
        self.film_name = film_name
        self.film_descr = film_descr
        self.film_writer = film_writer
        self.film_year = film_year
        self.upload_file()

    def upload_file(self):
        import os
        self.file_path = 'film_storage/' + self.film_name[0].upper() + '/' + self.film_name + '.txt'
        f_file = open(self.file_path, 'w')
        f_string = f'Name : {self.film_name}. Film year : {self.film_year}. Description : {self.film_descr}. Writer : {self.film_writer}'
        f_file.write(f_string)
        f_file.close()

    def get_film_address(self, film_name, film_year):
        self.storage_address = f'Path to file with film \"{self.film_name}\" -> {self.file_path}'
