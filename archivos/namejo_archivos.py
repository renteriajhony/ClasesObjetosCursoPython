try:
    archivo = open('archivos.txt', 'w', encoding='utf-8')
    archivo.write('Agregamos información al archivo')
    archivo.write('\n')
    archivo.write('Saludos')
except FileNotFoundError as error:
    print(error)
except Exception as error:
    print(error)
finally:
    archivo.close()