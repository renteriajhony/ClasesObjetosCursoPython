from unittest import result


class Arithmetic:

    def __init__(self, operator1=None, operator2=None):
        self.__operator1 = operator1 #Argumento privado
        self.__operator2 = operator2 #Argumento privado

    @property
    def operator1(self):
        return self.__operator1
    @operator1.setter
    def operator1(self, value):
        self.__operator1 = value

    @property
    def operator2(self):
        return self.__operator2

    @operator2.setter
    def operator2(self, value):
        self.__operator2 = value

    def sum(self):
        ":returns: __operator1 + __operator2 "
        result = self.__operator1 + self.__operator2
        print(f'SUMA: {result}')

    def sub(self):
        ":returns: __operator1 - __operator2 "
        result = self.__operator1 - self.__operator2
        print(f'RESTA: {result}')

    def mul(self):
        ":returns: __operator1 * __operator2 "
        result = self.__operator1 * self.__operator2
        print(f'MULTIPLICACION: {result}')

    def div(self):
        ":returns: __operator1 / __operator2 "
        result = self.__operator1 / self.__operator2
        print(f'DIVISION: {result}')

if __name__ == '__main__':
    arithmetic = Arithmetic(5, 7)
    arithmetic.sum()
    arithmetic.sub()
    arithmetic.mul()
    arithmetic.div()
    print('\n')
    arithmetic2 = Arithmetic(12, 16)
    arithmetic2.operator2 = 12
    arithmetic2.sum()
    arithmetic2.sub()
