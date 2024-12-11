from mundo_pc_herencia.computer import Computer
from mundo_pc_herencia.input_device import Mouse, Keyboard
from mundo_pc_herencia.monitor import Monitor
from mundo_pc_herencia.order import Order

mouse1 = Mouse('Genius','Bluetooth')
mouse2 = Mouse('Apple','Bluetooth')
mouse3 = Mouse('Delux','Cable')

keyboard1 = Keyboard('Genius', 'Bluetooth')
keyboard2 = Keyboard('Apple', 'Bluetooth')
keyboard3 = Keyboard('Delux', 'Cable')

monitor1 = Monitor('Genius', 29)
monitor2 = Monitor('Apple', 35)
monitor3 = Monitor('Delux', 45)


computer1 = Computer('Genius', monitor1, keyboard1, mouse1)
computer2 = Computer('Apple', monitor2, keyboard2, mouse2)
computer3 = Computer('Delux', monitor3, keyboard3, mouse3)

computers_order1 = [computer1, computer2]
order1 = Order(computers_order1)

order2 = Order([computer3])

print('*** Mundo Pc Aplicacion ***')

print(order1)
order1.add_computer(computer3)
print(order1)
print(order2)