class Book:
    counter_books: int = 0
    def __init__(self, title, author, gender):
        Book.counter_books += 1
        self.__id = Book.counter_books #Atributo privado
        self._title = title #Atributo protegido
        self._author = author #Atributo protegido
        self._gender = gender #Atributo protegido

    @property
    def id(self):
        return self.__id
    # @id.setter
    # def id(self, id):
    #     self._title = id

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        self._author = author

    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, gender):
        self._gender = gender