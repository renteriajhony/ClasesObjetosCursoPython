from library_company.book import Book
from library_company.library import Library

print('*** Bienvenidos a la Libreria Nacional ***')

# Creamos libreria
library = Library(name='Libreria nacional')
library2 = Library(name='AnimeTk')

# Creamos Libros
libro1 = Book('Cien años de soledad', 'Gabo', 'Ficción')
library.add_book(libro1)
libro2 = Book('Don quijote de la mancha', 'Miguel', 'Comedia')
library.add_book(libro2)
libro3 = Book('El amor en los tiempos de colera', 'Gabo', 'Ficción')
library.add_book(libro3)
libro4 = Book('Pedro Páramo', 'Juan', 'Ficción')
library.add_book(libro4)
libro5 = Book('Pantaleon y las visitadoras', 'Mario', 'Comedia')
library.add_book(libro5)
libro6 = Book('Dragon ball', 'JR', 'Ficción')
library2.add_book(libro6)
libro7 = Book('Naruto', 'JR', 'Ficción')
library2.add_book(libro7)

# Respondemos pregunta busqueda de libros por Autor
library.search_books_for_author('Gabo')
# Respondemos pregunta busqueda de libros por genero
library.search_books_for_gender('Ficción')
# Respondemos Mostrar todos los libros
library.show_all_books()

print('\n*** Bienvenidos a la Libreria AnimeTk ***')
library2.search_books_for_author('Mario')
library2.search_books_for_gender('Accion')
library2.show_all_books()