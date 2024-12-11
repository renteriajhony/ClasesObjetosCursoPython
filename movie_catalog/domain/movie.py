class Movie:
    def __init__(self, name: str) :
        self._name = name
    def __str__(self) :
        return self.name

    @property
    def name(self) :
        return self._name
    @name.setter
    def name(self, name) :
        self._name = name