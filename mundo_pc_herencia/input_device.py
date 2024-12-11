class InputDevice:
    def __init__(self, mark, type_input):
        self.mark = mark
        self.type_input = type_input

class Mouse(InputDevice):
    counter_mouse: int = 0
    def __init__(self, mark, type_input):
            Mouse.counter_mouse += 1
            self.id_mouse = Mouse.counter_mouse
            super().__init__(mark, type_input)

    def __str__(self):
            return f'Id: {self.id_mouse}, Mark: {self.mark}, Type: {self.type_input}'
class Keyboard(InputDevice):
    counter_keyboard: int = 0

    def __init__(self, mark, type_input):
        Keyboard.counter_keyboard += 1
        self.id_keyboard = Keyboard.counter_keyboard
        super().__init__(mark, type_input)

    def __str__(self):
            return f' Id: {self.id_keyboard}, Mark: {self.mark}, Type: {self.type_input}'