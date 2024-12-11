from mundo_pc_herencia.input_device import Keyboard, Mouse
from mundo_pc_herencia.monitor import Monitor


class Computer:
    counter_computer = 0
    def __init__(self, name: str, monitor: Monitor, keyboard: Keyboard, mouse: Mouse):
        Computer.counter_computer += 1
        self.id_computer = Computer.counter_computer
        self.name = name
        self.monitor = monitor
        self.keyboard = keyboard
        self.mouse = mouse

    def __str__(self):
        return f'''
        {self.id_computer} - {self.name}\t
        Monitor: {self.monitor}
        Keyboard: {self.keyboard}
        Mouse: {self.mouse}
        '''