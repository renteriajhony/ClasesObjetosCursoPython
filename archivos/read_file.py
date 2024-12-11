try:
    archivo = open('archivos.txt', 'r', encoding='utf-8')

    # print(archivo.readline())
    # print(archivo.readline())
    # print(archivo.read())\

    # #Iteramos el archivo
    # for line in archivo:
    #     print(line)

    #Leer todo el archivo y devolverlo como arreglo
    # print(archivo.readlines())
    # print(archivo.readlines()[1])

    #Crear una copia del archivo
    archivo_copia = open('copia.txt', 'w', encoding='utf-8')
    archivo_copia.write(archivo.read())
    print(archivo_copia.read())

except FileNotFoundError as error:
    print(error)
except Exception as error:
    print(error)
finally:
    archivo.close()
    archivo_copia.close()