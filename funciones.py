import random
import io
import os
import os.path
import pickle
from clase import *

def add_in_order(arreglo, registro): #se recorre el arreglo en forma secuencial y agrega el registro
    n = len(arreglo)
    pos = n
    if n == 0:
        arreglo.append(registro)
        return
    for i in range(n):
        if  registro.titulo < arreglo[i].titulo:
            pos = i
            break
    arreglo[pos:pos] = [registro]


def carga_arreglo(v):
    n = int(input("Cuantas peliculas desea cargar: "))
    n_random = ["Los valientes", "Harry Potter y La Piedra Filosofal", "El Señor de los Anillos", "El Alquimista", "El Código da Vinci", "Crepúsculo", "Lo que el viento se llevó", "Piense y hágase rico", "El diario de Ana Frank"]
    for i in range(n):
        cod = random.randint(1, 1000)
        nom = random.choice(n_random)
        impor = random.randint(1000, 1000000)
        tipo = random.randint(0, 9)
        pais = random.randint(0, 19)
        peli = Pelicula(cod, nom, impor, tipo, pais)
        add_in_order(v, peli)
    print("Peliculas cargadas......")
def to_string(registro):
    r = ""
    r += "{:<25}".format("| Codigo: " + str(registro.identificacion) )
    r += "{:<50}".format("| Nombre: " + str(registro.titulo))
    r += "{:<30}".format("| Importe invertido: " + str(registro.importe))
    r += "{:<30}".format("| Tipo: " + str(registro.tipo))
    r += "{:<30}".format("| Pais de origen " + str(registro.pais))
    return r

def bucar(arreglo):
    if len(arreglo) == 0:
        print("No hay datos cargados...")
        print()
        return

    nom= input("Ingrese el nombre de la pelicula que desea buscar: ")
    nom = nom.lower()
    n = len(arreglo)
    izq, der = 0, n -1
    while izq <= der:
        c = (izq + der) // 2
        if arreglo[c].titulo.lower() == nom:
            print("Pelicula encontrada.. \n")
            print("Ingrese el nuevo importe de la pelicula:")
            arreglo[c].importe = int(input(": "))
            print(to_string(arreglo[c]))
            print()
            return
        if nom < arreglo[c].titulo:
            der = c - 1
        else:
            izq = c + 1

    print("No hay una pelicula con ese nombre ingresado..")

    print()
    return -1
def busqueda_secuencial(arreglo):
    n = len(arreglo)
    x = int(input("Ingrese la identificacion de la pelicula que desea buscar: "))

    for i in range(n):
        if arreglo[i].identificacion == x:
            print(to_string(arreglo[i]))
    return -1

def crear_archivo_todos(v, fd):
    if len(v) == 0:
        print("Arreglo vacio")
        return
    m = open(fd, "wb")

    # pickle.dump(v, m)

    # Segunda forma en que carga los arreglos por separados
    n = int(input("Ingrese el tope de importe: "))
    for peli in v:
        if peli.pais != 10 and peli.importe < n:
            pickle.dump(peli, m)

    m.close()
    print("Se creo el archivo cocn exito")

def ver_archivos(fd):

    if not os.path.exists(fd):
        print("El archivo no existe")
        print()
        return
    print("Contenido actual del archivo")

    m = open(fd, "rb")

    #si el archivo contiene SOLO UN VECTOR
    # v = pickle.load(m)
    # print(v)
    # for i in v:
    #     display(i)

    ## SI CONTIENE MAS DE UN VECTOR
    # tama = os.path.getsize(fd)
    # while m.tell() < tama:
    #     v = pickle.load(m)
    #     for i in v:
    #         display(i)
    tama = os.path.getsize(fd)
    while m.tell() < tama:
        a = pickle.load(m)
        print(to_string(a))

    m.close()

def crear_matriz(filas, columnas):

    #primera forma de crear matriz
    # m1 = []
    # for f in range(n):
    #     m1.append([])
    #     for c in range(m):
    #         m1[f].append(None)
    #
    #
    # # Segunda forma de crer matriz
    m1 = [0] * filas
    for f in range(filas):
        m1[f] = [0] * columnas
    return m1
def imprimir_matriz(mat):
    for i in range(len(mat)):
        print("'", mat[i] ,"'")

def count_pelis(m2, arreglo):
    n = len(arreglo)
    for i in range(n):
        tipo = arreglo[i].tipo
        pais = arreglo[i].pais
        m2[tipo][pais] += 1


def recorrido_filas(m2):
    for f in range(len(m2)):
        for c in range(len(m2[f])):
            if m2[f][c] != 0:
                print("Pelicula/s del tipo " + str(f) + " en el pais " + str(c) + ":  " + str(m2[f][c]))

def imprimir_arreglo(arreglo):
    print()
    for i in range(len(arreglo)):
            print(to_string(arreglo[i]))
            print("-" * 200)
