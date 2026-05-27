
def registrar_libro(libros):
    print("\n=== REGISTRAR NUEVO LIBRO ===")
    titulo = input("Título del libro: ").strip()
    
    # Mejora leve: Validar que no quede vacío el título
    if not titulo:
        titulo = "Libro sin título"
        
    autor = input("Autor: ").strip()
    if not autor:
        autor = "Autor Anónimo"
        
    try:
        anio = int(input("Año de publicación: "))
    except ValueError:
        anio = 0
        
    nuevo_libro = {"titulo": titulo, "autor": autor, "anio": anio}
    libros.append(nuevo_libro)
    print(f"✅ ¡Libro '{titulo}' registrado con éxito!")

def eliminar_libro(libros):
    print("\n=== ELIMINAR UN LIBRO ===")
    if not libros:
        print("No hay libros para eliminar.")
        return
    titulo_eliminar = input("Ingrese el título del libro a borrar: ").lower().strip()
    for libro in libros:
        if libro["titulo"].lower() == titulo_eliminar:
            libros.remove(libro)
            print(f"🗑️ El libro '{libro['titulo']}' fue eliminado.")
            return
    print("❌ No se encontró ningún libro con ese título.")