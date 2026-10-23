
actual = None

while True:
    print("\n--- Historial ---")
    print("1. Visitar página")
    print("2. Retroceder")
    print("3. Avanzar")
    print("4. Mostrar página actual")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        pagina = input("Ingresa la página: ").strip()
        if pagina:
            nuevo = {"dato": pagina, "anterior": actual, "siguiente": None}
            if actual is not None:
                actual["siguiente"] = nuevo
            actual = nuevo
            print("Visitando:", pagina)
        else:
            print("Ingresa una página válida.")

    elif opcion == "2":
        if actual and actual["anterior"]:
            actual = actual["anterior"]
            print("Retrocediste a:", actual["dato"])
        else:
            print("No puedes retroceder.")

    elif opcion == "3":
        if actual and actual["siguiente"]:
            actual = actual["siguiente"]
            print("Avanzaste a:", actual["dato"])
        else:
            print("No puedes avanzar.")

    elif opcion == "4":
        print("Página actual:", actual["dato"] if actual else "Ninguna")

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción incorrecta.")
