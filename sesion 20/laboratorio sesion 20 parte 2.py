def descuento(precio, dto=0.10):
    return precio - (precio * dto)

print("El precio final es:", descuento(precio=int(input("Ingrese el precio:")), dto=float(input("Ingrese el descuento:"))))
