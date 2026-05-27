def mostrar_libros(libros):
    print("\n===== TODOS LOS LIBROS REGISTRADOS =====")
    if not libros:
        print("La biblioteca está vacía.")
        return
    print(f"📚 Total de libros: {len(libros)}\n")
    for i, libro in enumerate(libros, 1):
        print("-" * 40)
        print(f"{i}. Título: {libro['titulo']}\n   Autor: {libro['autor']}\n   Año: {libro['anio']}")
    print("-" * 40)


def buscar_libro(libros):
    print("\n=== BUSCAR LIBRO POR TÍTULO ===")
    busqueda = input("Ingrese el título a buscar: ").lower().strip()
    encontrado = False
    for libro in libros:
        if busqueda in libro["titulo"].lower():
            print(f"\n🔍 Encontrado -> Título: {libro['titulo']} | Autor: {libro['autor']} | Año: {libro['anio']}")
            encontrado = True
    if not encontrado:
        print("❌ No se encontró ningún libro con ese título.")
