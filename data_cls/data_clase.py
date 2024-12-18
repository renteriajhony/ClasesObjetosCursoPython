from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Persona:
    nombre: str
    apellido: str = None
    contador_persona: ClassVar[int] = 0

persona1 = Persona('Juan', 'Pricilla Price')
print(persona1)
print(f'{persona1!r}')

persona2 = Persona()
print(persona2)