from tabulate import tabulate
from backend.productos import leer_productos, buscar_producto
from utils.pausa import pausa
from utils.separador import separador
from utils.limpiar import limpiar

RUTA = "data/productos.xlsx"

def mostrar_productos():
    separador()
    print("LISTADO DE PRODUCTOS")
    separador()
    productos = leer_productos(RUTA)

    tabla = []
    for p in productos:
        tabla.append([p["id"], p["nombre"], p["precio"], p["cantidad"]])

    print(tabulate(tabla, headers=["ID", "Nombre", "Precio", "Cantidad"], tablefmt="grid"))
    separador()
    pausa()


def consultar_producto():
    separador()
    productos = leer_productos(RUTA)
    id_buscar = int(input("Ingrese ID: "))

    producto = buscar_producto(productos, id_buscar)

    if producto:
        separador()
        print("RESULTADO DE BÚSQUEDA")
        print(tabulate([[producto["id"], producto["nombre"], producto["precio"], producto["cantidad"]]],
              headers=["ID", "Nombre", "Precio", "Cantidad"], tablefmt="grid"))
    else:
        print("Producto no encontrado")
    separador()
    pausa()


def menu():
    limpiar()
    while True:
        separador()
        print("MENÚ DE OPCIONES")
        separador()
        print("\n1. Ver productos")
        print("2. Buscar producto")
        print("3. Salir")

        op = input("Opción: ")

        if op == "1":
            mostrar_productos()
        elif op == "2":
            consultar_producto()
        elif op == "3":
            limpiar()
            break
