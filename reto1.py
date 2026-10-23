
cabeza = cola = None

cantidad = int(input("¿Cuántos datos quieres ingresar?: "))

for i in range(cantidad):
    dato = input("Ingresa un dato: ")
    nuevo = {"dato": dato, "anterior": cola, "siguiente": None}

    if cola is not None:
        cola["siguiente"] = nuevo
    else:
        cabeza = nuevo
    cola = nuevo


def buscar(dato, actual, direccion):
    while actual is not None:
        if actual["dato"] == dato:
            return True
        actual = actual[direccion]
    return False


dato = input("¿Qué dato deseas buscar?: ")

print("Desde cabeza:", buscar(dato, cabeza, "siguiente"))
print("Desde cola:", buscar(dato, cola, "anterior"))
