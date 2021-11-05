

from clase import *
from funciones import *

# Productora
# Una empresa de producciones cinematográficas mantiene información sobre las distintas películas que tiene en desarrollo.
# Por cada película se registran los datos siguientes: número de identificación de la película (un número entero), título
# (una cadena), importe invertido en su producción, tipo de película (un valor entre 0 y 9 incluidos, de la forma 0: acción,
# 1: comedia, 2: drama, etc.) y un número para identificar el pais de origen de la película (un número entero entre 0 y 19
# incluidos) Se pide definir un tipo registro Pelicula con los campos que se indicaron, y un programa completo con menú de
# opciones para hacer lo siguiente:
#
# 1- Cargar los datos de n registros de tipo Pelicula en un arreglo de registros (cargue n por teclado). Puede cargar los
# datos manualmente, o puede generarlos aleatoriamente. El arreglo debe crearse de forma que siempre quede ordenado de
# menor a mayor, según el título de las películas.
#
# 2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea.
#
# 3 - Buscar en el arreglo creado en el punto 1 un registro en el cual el titulo de la pelicula sea igual a nom (cargar
# nom por teclado). Si existe, mostrar por pantalla los datos, previamente modicar el importe con un valor imp (cargar imp
# por teclado). Si no existe, informar con un mensaje. La busqueda debe detenerse al encontrar el primer registro que
# coincida con el titulo
#
# 4- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todas las películas cuyo pais
# de origen no sea el 10 y cuyo importe invertido sea menor a un valor x que se carga por teclado.
#
# 5- Mostrar el archivo creado en el punto 3, a razón de un registro por línea en la pantalla.
#
# 6- Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación de la película sea igual
# a num (cargar num por teclado). Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, informar
# con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.
#
#
# 7- Usando el arreglo creado en el punto 1, determine la cantidad de películas de cada posible tipo por cada posible
# pais de origen (o sea, 10 * 20 = 200 contadores en una matriz de conteo). Muestre sólo los resultados que sean
# diferentes de 0.




def main():
    op = 0
    menu = """
    Menu:
        1). Cargar los datos
        2). Mostrar el arreglo creado
        3). Buscar en el arreglo creado por nombre
        4). crear un archivo de registros 
        5). Mostrar el archivo creado
        6). Buscar en el arreglo creado por identificacion
        7). Muestra de los resultados por tipo y pais
        8). Salir
    
    """


    peliculas = []
    fd = "Peliculas.dat"
    paises = 20
    tipos = 10


    while op >= 0:
        print("-" * 100)
        print(menu)
        print("-" * 100)
        op = int(input("Ingrese una opcion: "))
        if op == 1:
            carga_arreglo(peliculas)
        if 0 < len(peliculas):
            if op == 2:
                imprimir_arreglo(peliculas)
            elif op == 3:
                bucar(peliculas)
            elif op == 4:
                crear_archivo_todos(peliculas, fd)
            elif op == 5:
                ver_archivos(fd)
            elif op == 6:
                busqueda_secuencial(peliculas)
            elif op == 7:
                matriz = crear_matriz(tipos, paises)
                count_pelis(matriz, peliculas)
                recorrido_filas(matriz)
            elif op == 8:
                break
            elif op > 8:
                print("Por favor.....Elija una de las opciones correctas.... \n")
            else:
                pass

        else:
            print("\nPor favor..... primero cargue elementos al registro")


if __name__ == '__main__':
    main()
