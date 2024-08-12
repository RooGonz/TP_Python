from principal import *
from configuracion import *
import random
import math
from extras import *

def sacadorbarra (cadena):
    cadenaNva=""
    for i in range(len(cadena)):
        if i == len(cadena)-1:
            cadenaNva+=","
        else:
            cadenaNva+=cadena[i]
    return cadenaNva

def sepadorCadena(cadena):
    cadena1=sacadorbarra(cadena)
    listaNva=[]
    elemento=""
    cont=0
    for letra in cadena1:
        if letra != ",":
            elemento+=letra
        else:
            if cont == 0:
                listaNva.append(elemento)
                elemento=""
                cont+=1
            else:
                listaNva.append(int(elemento))
                elemento=""
                cont+=1
        if cont > 2:
            cont=0

    return listaNva

def lectura ():
    archivo = open("productos.txt", "r")
    lista_producto= []
    for linea in archivo.readlines():
        listaPeq=sepadorCadena(linea)
        lista_producto.append(listaPeq)

    archivo.close()
    return lista_producto

def buscar_producto (lista):
    producto=[]
    nrorandom=random.randint(0, len(lista)-1)
    listacort=lista[nrorandom]
    nombre=listacort[0]
    producto.append(nombre)
    nrorandom2=random.randint(1,2)
    tipoProd=""
    if nrorandom2 == 1:
        tipoProd= (" (Economico)")
    else:
        tipoProd= (" (Premium)")
    producto.append(tipoProd)
    precio=listacort[nrorandom2]
    producto.append(precio)

    return producto

def esUnPrecioValido (precio,lista,margen):
    cont=0
    for i in range(len(lista)):
        precio1=lista[i][1]
        precio2=lista[i][2]
        if abs(precio1 - precio) <= margen or abs(precio2 - precio) <= margen:
            cont+=1
    if cont>=3:
        return True
    else:
        return False

def dameProducto (lista, margen):
    seguir=True
    while seguir:
        producto=buscar_producto(lista)
        precio=producto[2]
        if esUnPrecioValido (precio,lista,margen) == True:
            return producto

def procesar (producto_principal, producto_candidato, margen):
    canasta=0
    if producto_principal[2] == producto_candidato[2] or (abs(producto_principal[2]-producto_candidato[2]) <= margen):
        canasta+=producto_principal[2]
    return canasta

def cantRep(elem, lista):
    cont = 0
    for elem1 in lista:
        if elem1 == elem:
            cont = cont + 1
    return cont

def listaSinRep(lista):
    i = 0
    while i < len(lista):
        if lista[i] in lista and cantRep(lista[i], lista) > 1:
            lista.pop(i)
        else:
            i = i + 1

def dameProductosAleatoriosFACIL(producto, lista, margen):
    productos=[]
    productos.append(producto)
    
    while len(productos)<4:
        prod_ganador=buscar_producto(lista)
        if procesar(producto,prod_ganador,margen)!= 0:
            productos.append(prod_ganador)
            listaSinRep(productos)
    while len(productos)<6:
        productos.append(buscar_producto(lista))
        listaSinRep(productos)

    posicionCero= [productos[0]]
    productos.pop(0)
    random.shuffle(productos)
    productos.insert(0,producto)

    return productos

def dameProductosAleatoriosNORMAL(producto, lista, margen):
    productos=[]
    productos.append(producto)
    
    while len(productos)<3:
        prod_ganador=buscar_producto(lista)
        if procesar(producto,prod_ganador,margen)!= 0:
            productos.append(prod_ganador)
            listaSinRep(productos)
    while len(productos)<6:
        productos.append(buscar_producto(lista))
        listaSinRep(productos)

    posicionCero= [productos[0]]
    productos.pop(0)
    random.shuffle(productos)
    productos.insert(0,producto)

    return productos

def dameProductosAleatoriosDIFICIL(producto, lista, margen):
    productos=[]
    productos.append(producto)
    
    while len(productos)<2:
        prod_ganador=buscar_producto(lista)
        if procesar(producto,prod_ganador,margen)!= 0:
            productos.append(prod_ganador)
            listaSinRep(productos)
    while len(productos)<6:
        productos.append(buscar_producto(lista))
        listaSinRep(productos)

    posicionCero= [productos[0]]
    productos.pop(0)
    random.shuffle(productos)
    productos.insert(0,producto)

    return productos