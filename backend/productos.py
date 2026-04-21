import openpyxl

def leer_productos(ruta):
    productos = []
    archivo = openpyxl.load_workbook(ruta)
    hoja = archivo.active

    for fila in hoja.iter_rows(min_row=2, values_only=True):
        productos.append({
            "id": fila[0],
            "nombre": fila[1],
            "precio": fila[2],
            "cantidad": fila[3]
        })

    return productos


def buscar_producto(productos, id_buscar):
    for p in productos:
        if p["id"] == id_buscar:
            return p
    return None
