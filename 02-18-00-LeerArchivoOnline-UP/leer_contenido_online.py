# Leer contenido online
import urllib
from urllib.request import urlopen

# Debido a cambios en la libreria se deben hacer los siguientes cambios:
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

with urlopen(peticion) as mensaje:
    contenido = mensaje.read().decode('utf-8')
    print(contenido)

with open('nuevo_archivo.txt','w', encoding='utf-8') as archivo:
    archivo.write(contenido)


# Leer palabras de u archivo
palabras = []
with urlopen(peticion) as mensaje:
    for line in mensaje.readlines():
        contenido = line.decode('utf-8').split()
        for palabra in contenido:
            palabras.append(palabra)
print(palabras)
# with open('nuevo_archivo2.txt', 'w', encoding='utf-8') as archivo:
#     archivo.write(contenido)
