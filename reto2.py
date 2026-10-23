
cabeza = cola = None

cantidad = int(input("¿Cuántos datos quieres ingresar?: "))

for i in range(cantidad):
    dato = input("Ingresa un dato: ")
    nuevo = {"dato": dato, "anterior": cola, "siguiente": None}

    if cola is None:
        cabeza = nuevo
    else:
        cola["siguiente"] = nuevo

    cola = nuevo


def insertar_despues(referencia, dato):
    global cola
    actual = cabeza

    while actual is not None:
        if actual["dato"] == referencia:
            nuevo = {
                "dato": dato,
                "anterior": actual,
                "siguiente": actual["siguiente"]
            }

            if actual["siguiente"] is None:
                cola = nuevo
            else:
                actual["siguiente"]["anterior"] = nuevo

            actual["siguiente"] = nuevo
            return True

        actual = actual["siguiente"]

    return False


referencia = input("¿Después de qué dato quieres insertar?: ")
dato = input("¿Qué dato deseas insertar?: ")

print("Insertado:", insertar_despues(referencia, dato))

print("Lista final:")
actual = cabeza
while actual is not None:
    print(actual["dato"], end=" <-> " if actual["siguiente"] else "\n")
    actual = actual["siguiente"]

if cabeza is None:
    print("(Lista vacía)")
