import os

from movie_catalog.domain.movie import Movie


class MovieCatalogService:
    def __init__(self, path_file: str):
                self._path_file = path_file
                with open(self.path_file, 'a', encoding='utf-8'):
                    pass


    @property
    def path_file(self) -> str:
        return self._path_file
    @path_file.setter
    def path_file(self, path_file: str):
        self._path_file = path_file

    def add_movie(self, movie: Movie):
        if movie.name.strip() == '':
            print('Pelicula no pudo ser agregada')
        else:
            with open(self.path_file, 'a', encoding='utf-8') as file:
                file.write(movie.name)
                file.write("\n")
            print(f'Película: {movie.name} *** Agregada\n')

    def show_movie(self):
        with open(self.path_file, 'r', encoding='utf-8') as file:
            file_read = file.read()
            if file_read == '':
                print('No se encontraron películas')
            print(file_read)

    def delete_movie(self, movie_id: int):
        print('Eliminar Película'.center(50, '-'))
        copy_content_file = []
        with open(self.path_file, 'r', encoding='utf-8') as file:
            copy_content_file = file.readlines()
            copy_content_file.pop(movie_id)
        with open(self.path_file, 'w', encoding='utf-8') as file:
            file.writelines(copy_content_file)

    def delete_all_movies(self):
        os.remove(self.path_file)

if __name__ == '__main__':
    movie = Movie('En busca de la felicidad')
    movie2 = Movie('Escritores de la libertad')
    movie3 = Movie('')
    movie4 = Movie('Juego de honor')

    movie_catalog = MovieCatalogService('peliculasTest.txt')
    movie_catalog.add_movie(movie)
    movie_catalog.add_movie(movie2)
    movie_catalog.add_movie(movie3)
    movie_catalog.add_movie(movie4)
    # movie_catalog.show_movie()
    movie_catalog.delete_movie(1)