import os

inventario = []
opcion = 0

def borrar_pantalla(): 
    columnas, filas = os.get_terminal_size()
    print("\n" * filas)

def buscar_productos(criterio, valor):
    resultados = []
    for producto in inventario:
        if producto[criterio] == valor:
            resultados.append(producto)
    return resultados

while opcion != 6:
    print("Sistema de Administración de Inventario para la Ferreteria de Karibay")
    print("")
    print("Seleccione una opción:")
    print("")
    print("1) Agregar producto")
    print("2) Eliminar producto")
    print("3) Buscar producto")
    print("4) Actualizar producto")
    print("5) Mostrar inventario")
    print("6) Salir del sistema")
    print("")

    opcion = int(input("Ingrese su opción: "))

    if opcion >= 1 and opcion <= 6:
        borrar_pantalla()

        if opcion == 1:
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            cantidad = int(input("Ingrese la cantidad en stock del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = {
                "nombre": nombre,
                "categoria": categoria,
                "cantidad": cantidad,
                "precio": precio
            }
            existe = False
            for p in inventario:
                if p["nombre"] == nombre:
                    existe = True
                    break
            if not existe:
                inventario.append(producto)
                inventario.sort(key=lambda p: p["nombre"])
                print("Producto agregado con éxito.")
            else:
                print("El producto ya existe en el inventario.")

        elif opcion == 2:
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            encontrado = False
            for i in range(len(inventario)):
                if inventario[i]["nombre"] == nombre:
                    encontrado = True
                    break
            if encontrado:
                inventario.pop(i)
                print("Producto eliminado con éxito.")
            else:
                print("El producto no existe en el inventario.")

        elif opcion == 3:
            criterio = input("Escribe el criterio de búsqueda que deseas utilizar (nombre o categoria): ")
            if criterio == "nombre" or criterio == "categoria":
                valor = input("Ingrese el valor a buscar: ")
                resultados = buscar_productos(criterio, valor)
                if len(resultados) > 0:
                    print(f"Se encontraron {len(resultados)} productos con {criterio} = {valor}:")
                    print(f"{'Nombre':<20}{'Categoría':<20}{'Cantidad':<10}{'Precio':<10}")
                    for r in resultados:
                        print(f"{r['nombre']:<20}{r['categoria']:<20}{r['cantidad']:<10}{r['precio']:<10.2f}")
                else:
                    print("No se encontraron productos con ese criterio y valor.")
            else:
                print("El criterio de búsqueda no es válido.")

        elif opcion == 4:
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            encontrado = False
            for i, producto in enumerate(inventario):
                if producto["nombre"] == nombre:
                    encontrado = True
                    break
            if encontrado:
                print("Ingrese los nuevos datos del producto. Deje en blanco para mantener el valor actual.")
                nuevo_nombre = input(f"Nuevo nombre ({nombre}): ") or nombre
                nueva_categoria = input(f"Nueva categoría ({inventario[i]['categoria']}): ") or inventario[i]['categoria']
                nueva_cantidad = input(f"Nueva cantidad ({inventario[i]['cantidad']}): ")
                nuevo_precio = input(f"Nuevo precio ({inventario[i]['precio']}): ")

                # Actualizar solo si se ingresan nuevos valores
                inventario[i]['nombre'] = nuevo_nombre if nuevo_nombre else inventario[i]['nombre']
                inventario[i]['categoria'] = nueva_categoria if nueva_categoria else inventario[i]['categoria']
                inventario[i]['cantidad'] = int(nueva_cantidad) if nueva_cantidad else inventario[i]['cantidad']
                inventario[i]['precio'] = float(nuevo_precio) if nuevo_precio else inventario[i]['precio']

                print("Producto actualizado con éxito.")
            else:
                print("El producto no existe en el inventario.")

        elif opcion == 5:
            if len(inventario) > 0:
                print("Inventario actual:")
                print(f"{'Nombre':<20}{'Categoría':<20}{'Cantidad':<10}{'Precio':<10}")
                for producto in inventario:
                    print(f"{producto['nombre']:<20}{producto['categoria']:<20}{producto['cantidad']:<10}{producto['precio']:<10.2f}")
            else:
                print("El inventario está vacío.")