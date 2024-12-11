from mundo_pc_herencia.computer import Computer


class Order:
    counter_order = 0
    def __init__(self, computers:list[Computer]):
        Order.counter_order += 1
        self.counter_order = Order.counter_order
        self.computers = computers

    def add_computer(self, computer: Computer):
        self.computers.append(computer)

    def __str__(self):
        computers_srt = ''
        for computer in self.computers :
            computers_srt += str(computer)
        return (f'Nueva orden  \n\tNumero de orden: {self.counter_order}  '
                f'\n\tComputadoras: {computers_srt} ')