from tabulate import tabulate
from backend.productos import leer_productos, buscar_producto, crear_producto, actualizar_producto, eliminar_producto
from utils.pausa import pausa

RUTA = "data/productos.xlsx"

def mostrar_productos():
    productos = leer_productos(RUTA)

    tabla = []
    for p in productos:
        tabla.append([p["id"], p["nombre"], p["precio"], p["cantidad"]])

    print(tabulate(tabla, headers=["ID", "Nombre", "Precio", "Cantidad"], tablefmt="grid"))


def consultar_producto():
    productos = leer_productos(RUTA)
    id_buscar = int(input("Ingrese ID: "))

    producto = buscar_producto(productos, id_buscar)

    if producto:
        print(tabulate([[producto["id"], producto["nombre"], producto["precio"], producto["cantidad"]]],
              headers=["ID", "Nombre", "Precio", "Cantidad"], tablefmt="grid"))
    else:
        print("Producto no encontrado")


def solicitar_producto():
    id_producto = int(input("Ingrese ID: "))
    nombre = input("Ingrese nombre: ")
    precio = float(input("Ingrese precio: "))
    cantidad = int(input("Ingrese cantidad: "))

    return id_producto, nombre, precio, cantidad


def crear():
    id_producto, nombre, precio, cantidad = solicitar_producto()
    resultado = crear_producto(RUTA, id_producto, nombre, precio, cantidad)

    if resultado == True:
        print("Producto creado exitosamente")
    else:
        print("El producto ya existe")

    pausa()


def actualizar():
    id_producto, nombre, precio, cantidad = solicitar_producto()
    resultado = actualizar_producto(RUTA, id_producto, nombre, precio, cantidad)

    if resultado == True:
        print("Producto actualizado exitosamente")
    else:
        print("Producto no encontrado")

    pausa()


def eliminar():
    id_producto = int(input("Ingrese ID a eliminar: "))
    resultado = eliminar_producto(RUTA, id_producto)

    if resultado == True:
        print("Producto eliminado exitosamente")
    else:
        print("Producto no encontrado")

    pausa()


def menu():
    while True:
        print("\n1. Ver productos")
        print("2. Buscar producto")
        print("3. Crear producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        op = input("Opción: ")

        if op == "1":
            mostrar_productos()
        elif op == "2":
            consultar_producto()
        elif op == "3":
            crear()
        elif op == "4":
            actualizar()
        elif op == "5":
            eliminar()
        elif op == "6":
            break
