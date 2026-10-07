cantidad = input("Cantidad de elementos: ")
precio = input("Precio: ")

print(type(cantidad))
print(type(precio))

cantidad_entero = int(cantidad)
precio_float = float(precio)

print(type(cantidad_entero))
print(type(precio_float))

total = precio_float * cantidad_entero

print(round(total, 2))