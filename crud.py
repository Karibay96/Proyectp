import json

def crear(producto, path):
    productos = {}
    with open(path, "r") as file:
        productos = json.load(file)

    for p in productos["data"]:
        if p["nombre"].lower() == producto["nombre"].lower():
            #El artículo ya existe en el inventario.
            return True

    productos["data"].append(producto)

    with open(path, "w") as file:
        json.dump(productos, file, indent=4)

def eliminar(nombre, path):
    productos = {}
    with open(path, "r") as file:
        productos = json.load(file)

    encontrado = False
    for i in range(len(productos["data"])):
        if productos["data"][i]["nombre"].lower() == nombre.lower():
            encontrado = True
            del productos["data"][i]
            break

    if not encontrado:
        print ("El artículo no existe en el inventario.")

    with open(path, "w") as file:
        json.dump(productos, file, indent=4)

def buscar(nombre, path):
    productos = {}
    with open(path, "r") as file:
        productos = json.load(file)

    encontrado = False
    for p in productos["data"]:
        if p["nombre"].lower() == nombre.lower():
            encontrado = True
            print("-" * 40)
            print(f"Nombre: {p['nombre']}")
            print(f"Categoría: {p['categoria']}")
            print(f"Cantidad: {p['cantidad']}")
            print(f"Precio: {p['precio']}")
            print("-" * 40)
            break

    if not encontrado:
        print ("El artículo no existe en el inventario.")


def modificar(nombre, nuevos_datos, path):
    productos = {}
    with open(path, "r") as file:
         productos = json.load(file)

    encontrado = False
    for i in range(len(productos["data"])):
        if productos["data"][i]["nombre"].lower() == nombre.lower():
            encontrado = True
            productos["data"][i].update(nuevos_datos)
            break

    if not encontrado:
        print ("El artículo no existe en el inventario.")
        return

    with open(path, "w") as file:
        json.dump(productos, file, indent=4)

def mostrar(path):
    productos = {}
    with open(path, "r") as file:
        productos = json.load(file)

    print("Listado de productos:")
    print("-" * 40)
    for p in productos["data"]:
        print(f"Nombre: {p['nombre']}")
        print(f"Categoría: {p['categoria']}")
        print(f"Cantidad: {p['cantidad']}")
        print(f"Precio: {p['precio']}")
        print("-" * 40)

