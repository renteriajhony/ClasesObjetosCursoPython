from movie_catalog.domain.movie import Movie
from movie_catalog.service.movie_catalog_service import MovieCatalogService

print('CATALOGO DE PELICULAS'.center(100,'*'))
move_catalog_service = MovieCatalogService('peliculas.txt')
while True:
    print(f''' MENU
     1 - Agregar película
     2 - Listar películas
     3 - Eliminar película por posicion
     4 - Eliminar archivo de películas
     5 - Salir
    ''')
    opcion_menu = int(input('Seleccione una opción del menu (1 - 5): '))

    if opcion_menu == 1:
        print('Agregar de Película'.center(50, '-'))
        movie_name = input('Nombre de película: ')
        movie = Movie(movie_name)
        move_catalog_service.add_movie(movie)
    elif opcion_menu == 2:
        print('Catálogo de Películas'.center(50, '-'))
        move_catalog_service.show_movie()
    elif opcion_menu == 3:
        posc_movie = int(input('Pelicula a eliminar: '))
        move_catalog_service.delete_movie(posc_movie)
    elif opcion_menu == 4:
        move_catalog_service.delete_all_movies()
    elif opcion_menu == 5:
        break