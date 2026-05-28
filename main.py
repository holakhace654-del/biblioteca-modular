import consultas
import modificaciones

def menu_principal():
    libros = [] 
    while True:
        print("\n===== BIBLIOTECA GENERAL =====")
        print("1. Registrar libro")
        print("2. Mostrar libros")
        print("3. Buscar libro")
        print("4. Eliminar libro")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            modificaciones.registrar_libro(libros) 
        elif opcion == "2":
            consultas.mostrar_libros(libros)       
        elif opcion == "3":
            consultas.buscar_libro(libros)         
        elif opcion == "4":
            modificaciones.eliminar_libro(libros)  
        elif opcion == "5":
            print("\n👋 Saliendo del sistema grupal. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
