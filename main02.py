import os

from tooladmin.crud import crear, eliminar, buscar, modificar, mostrar

def menu():
    opcion = 0
    while opcion != 7:
        mostrar("productos.json")
        print("-" * 40)
        print("Sistema de Administración de Inventario")
        print("para la Farmacia de Karibay")
        print("-" * 40)
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        print("-" * 40)

        opcion = int(input("Seleccione una opción: "))
        if type(opcion) == int:
            if opcion == 1:
                nombre = input("Ingrese el nombre del producto: ")
                categoria = input("Ingrese la categoría del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))

                producto = {
                    "nombre": nombre,
                    "categoria": categoria,
                    "cantidad": cantidad,
                    "precio": precio
                }

                creado = crear(producto, "productos.json")
                if creado != True:
                    print("Producto creado exitosamente.")
                    mostrar("productos.json")
                else:
                    mostrar("productos.json")
                    pass
                    #print("El producto ya existe en el inventario.")

            elif opcion == 2:
                nombre = input("Ingrese el nombre del producto a buscar: ")
                producto = buscar(nombre, "productos.json")
                if producto :
                    print("-" * 40)
                    for k, v in producto.items():
                        print(f"{k}: {v}")
                    print("-" * 40)
                else:
                    print("El producto no se encuentra en el inventario.")

            elif opcion == 3:
                nombre = input("Ingrese el nombre del producto a modificar: ")
                nuevos_datos = {}

                categoria = input("¿Desea modificar la categoría? (s/n): ")
                if categoria.lower() == "s":
                    nuevos_datos["categoria"] = input("Ingrese la nueva categoría: ")

                precio = input("¿Desea modificar el precio? (s/n): ")
                if precio.lower() == "s":
                    nuevos_datos["precio"] = float(input("Ingrese el nuevo precio: "))

                cantidad = input("¿Desea modificar la cantidad? (s/n): ")
                if cantidad.lower() == "s":
                    nuevos_datos["cantidad"] = float(input("Ingrese la nueva cantidad: "))

                actualizado = modificar(nombre, nuevos_datos, "productos.json")
                if actualizado:
                    print("El producto no se encuentra en el inventario.")
                    mostrar("productos.json")
                else:
                    print("Producto modificado exitosamente.")
                    mostrar("productos.json")

            elif opcion == 4:
                nombre = input("Ingrese el nombre del producto a eliminar: ")
                eliminado = eliminar(nombre, "productos.json")
                if eliminado:
                    print("El producto no se encuentra en el inventario.")
                    print("Verifique el nombre del producto e intente nuevamente.")
                    mostrar("productos.json")
                else:
                    print("Producto eliminado exitosamente.")
                    mostrar("productos.json")
            else:
                print("¡Gracias por usar el Sistema de Administración de Inventario para la Farmacia de Karibay!")
                break

        else:
            print("Opción no válida. Ingrese un número entre 1 y 5 y valores numericos.")


if __name__ == "__main__":
    menu()