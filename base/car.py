
class Car:
    def __init__(self, mark, model, color):
        self._mark = mark #Atributi publico sin _
        self._model = model #Atributi protegido un _
        self._color = color #Atributi privado dos __
    def drive(self):
        print(f''' Driving the car:
         Mark: {self._mark}
         Model: {self._model}
         Color: {self._color}
        ''')

    # def get_mark(self):
    #     return self._mark
    @property
    def mark(self):
        return self._mark
    @mark.setter
    def mark(self, mark):
        self._mark = mark

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

if __name__ == '__main__':
    # Crear primer carrro
    car1 = Car('Toyota', 'Yaris', 'Blanco')
    car1.drive()
    car1.mark ='Maceraty'
    car1.model = 'Z900'
    car1.color = 'Negro'
    car1.drive()