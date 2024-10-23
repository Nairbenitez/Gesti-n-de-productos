import os

productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto:").strip()
    if any(p["nombre"].lower() == nombre.lower() for p in productos):
        print(f"Ya existe un producto con el nombre '{nombre}'")
        return

    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
                continue

            cantidad = int(input("Introduce la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue

            break
        except ValueError:
            print("Por favor, introduce números válidos.")

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(producto)
    print(f"Producto '{nombre}' añadido correctamente.")
    guardar_datos()

def ver_productos():
    if not productos:
        print("No hay productos registrados.")
        return
    print("Lista de productos:")
    print("_" * 50)
    for producto in productos:
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        print("_" * 50)

def actualizar_producto():
    nombre = input("Introduce el nombre del producto que deseas actualizar: ").strip()
    encontrado = False

    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            encontrado = True
            while True:
                print("1: Actualizar nombre")
                print("2: Actualizar precio")
                print("3: Actualizar cantidad")
                print("4: Volver al menú")
                opcion = input("Selecciona una opción:")

                if opcion == "1":
                    nuevo_nombre = input("Introduce el nuevo nombre: ").strip()
                    if any(p["nombre"].lower() == nuevo_nombre.lower() for p in productos if p != producto):
                        print("Ya existe un producto con ese nombre.")
                        continue
                    producto["nombre"] = nuevo_nombre
                    print("Nombre actualizado correctamente.")

                elif opcion == "2":
                    try:
                        nuevo_precio = float(input("Introduce el nuevo precio:"))
                        if nuevo_precio < 0:
                            print("El precio no puede ser negativo.")
                            continue
                        producto["precio"] = nuevo_precio
                        print("Precio actualizado correctamente.")
                    except ValueError:
                        print("Por favor, introduce un precio válido.")

                elif opcion == "3":
                    try:
                        nueva_cantidad = int(input("Introduce la nueva cantidad:"))
                        if nueva_cantidad < 0:
                            print("La cantidad no puede ser negativa.")
                            continue
                        producto["cantidad"] = nueva_cantidad
                        print("Cantidad actualizada correctamente.")
                    except ValueError:
                        print("Por favor, introduce una cantidad válida.")

                elif opcion == "4":
                    break
                else:
                    print("Opción no válida.")

            guardar_datos()
            break

    if not encontrado:
        print(f"No se encontró el producto '{nombre}'.")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto que deseas eliminar:").strip()

    for i, producto in enumerate(productos):
        if producto["nombre"].lower() == nombre.lower():
            del productos[i]
            print(f"Producto '{nombre}' eliminado correctamente.")
            guardar_datos()
            return

    print(f"No se encontró el producto '{nombre}'.")

def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados correctamente.")

def cargar_datos():
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})
        print("Datos cargados correctamente.")
    else:
        print("No se encontraron datos previos.")

def menu():
    cargar_datos()
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()
 
