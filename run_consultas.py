from consultas import mostrar_libros, buscar_libro


def main():
    libros = [
        {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "anio": 1967},
        {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "anio": 1605},
    ]

    while True:
        print("\n=== MENÚ ===")
        print("1) Mostrar libros")
        print("2) Buscar libro por título")
        print("3) Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            mostrar_libros(libros)
        elif opcion == "2":
            buscar_libro(libros)
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta otra vez.")


if __name__ == "__main__":
    main()
