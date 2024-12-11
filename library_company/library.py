from library_company.book import Book


class Library:
    def __init__(self, name):
        self._name = name
        self._books: [Book] = []

    @property
    def name(self):
        return self._name

    @name.setter
    def gender(self, name):
        self._name = name


    def add_book(self, book: Book):
        """
        Agrega un nuevo libro a la biblioteca
        :param book
        """
        self._books.append(book)
        # print(f'\tLibro agregado con id {book.id}')

    def search_books_for_author(self, author: str):
        """
        Busca un libro por autor y muestra su detalle
        :param author:
        """
        is_found = False
        for book in self._books:
                if book.author.lower() == author.lower():
                    if not is_found:
                        print(f'\nLibros del autor: { author }')
                    is_found = True
                    self.show_book(book)
        if not is_found:
                print(f'\nNo se encontraron libros para el autor: { author }')

    def search_books_for_gender(self, gender: str):
        """
        Busca un libro por genero y muestra su detalle
        :param gender:
        """
        is_found = False
        for book in self._books:
            if book.gender.lower() == gender.lower():
                if not is_found:
                    print(f'\nLibros del genero: {gender}')
                is_found = True
                self.show_book(book)
        if not is_found:
            print(f'\nNo se encontraron libros para este genero: {gender}')

    def show_all_books(self):
        """
        Muestra el detalle de todos los libros de la biblioteca
        """
        print(f'\nTodos los libros de la Biblioteca: {self.name}')
        for book in self._books:
            self.show_book(book)

    def show_book(self, book: Book):
        """
        Muestra el detalle de un libro de la biblioteca
        :param book:
        :return:
        """
        print(f'\tLibro ->  Title: {book.title}, Author: {book.author}, Gender: {book.gender}')