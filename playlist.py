# ==========================================
# FUNCIONES DE VALIDACIÓN
# ==========================================

def validar_nombre(nombre):
    """Retorna True si el nombre no está vacío, no son solo espacios y tiene >= 2 caracteres."""
    if len(nombre.strip()) >= 2:
        return True
    return False


def validar_minutos(minutos):
    """Retorna True si los minutos son un entero >= 2."""
    if minutos >= 2:
        return True
    return False


def validar_descargas(descargas):
    """Retorna True si las descargas son un entero > 0."""
    if descargas > 0:
        return True
    return False


# ===========================================
# FUNCIONES DE MENÚ
# ===========================================

def mostrar_menu():
    """Muestra las opciones del menú principal en pantalla."""
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Mostrar canciones")
    print("2. Actualizar populares")
    print("3. Eliminar canción")
    print("4. Buscar canción")
    print("5. Agregar canción")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    """Lee, valida con try-except y retorna la opción numérica elegida por el usuario."""
    opcion = 0
    while opcion < 1 or opcion > 6:
        try:
            opcion = int(input("Ingrese una opción (1-6): "))
            if opcion < 1 or opcion > 6:
                print("Error: Debe ingresar un número entre 1 y 6.")
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número entero.")
            opcion = 0
    return opcion


# ==========================================
# FUNCIONES DE GESTIÓN DE PLAYLIST
# ==========================================

def actualizar_populares(playlist):
    """Opción 2: Actualiza el campo 'popular' de cada canción según sus descargas (> 500)."""
    for cancion in playlist:
        if cancion["descargas"] > 500:
            cancion["popular"] = True
        else:
            cancion["popular"] = False


def mostrar_canciones(playlist):
    """Opción 1: Actualiza populares y muestra el listado formateado de canciones."""
    actualizar_populares(playlist)
    
    if len(playlist) == 0:
        print("\nLa playlist está vacía.")
    else:
        print("\n=== LISTA DE CANCIONES ===")
        for cancion in playlist:
            estado = "POPULAR" if cancion["popular"] else "ESTÁNDAR"
            print(f"Nombre: {cancion['nombre']}")
            print(f"Duración (min): {cancion['minutos']}")
            print(f"Descargas: {cancion['descargas']}")
            print(f"Estado: {estado}")
            print("--------------------------------------------")


def buscar_cancion(playlist, nombre_buscar):
    """Opción 4: Busca coincidencia exacta (case-sensitive) y retorna el índice o -1."""
    for i in range(len(playlist)):
        if playlist[i]["nombre"] == nombre_buscar:
            return i
    return -1


def agregar_cancion(playlist):
    """Opción 5: Solicita datos, los valida con sus funciones y agrega el diccionario si todo es válido."""
    print("\n--- AGREGAR NUEVA CANCIÓN ---")
    nombre = input("Ingrese el nombre de la canción: ")
    
    if not validar_nombre(nombre):
        print("Error: El nombre no puede estar vacío ni ser solo espacios, y debe tener al menos 2 caracteres.")
        return

    try:
        minutos = int(input("Ingrese la duración en minutos: "))
    except ValueError:
        print("Error: La duración debe ser un número entero.")
        return

    if not validar_minutos(minutos):
        print("Error: Los minutos deben ser un número entero mayor o igual a 2.")
        return

    try:
        descargas = int(input("Ingrese el número de descargas: "))
    except ValueError:
        print("Error: Las descargas deben ser un número entero.")
        return

    if not validar_descargas(descargas):
        print("Error: Las descargas deben ser un número entero mayor que 0.")
        return

    # Si todos los datos son válidos, se crea el diccionario y se agrega a la lista
    nueva_cancion = {
        "nombre": nombre,
        "minutos": minutos,
        "descargas": descargas,
        "popular": False
    }
    playlist.append(nueva_cancion)
    print(f"Canción '{nombre}' agregada exitosamente a la playlist.")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():
    playlist = []
    opcion = 0

    while opcion != 6:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            mostrar_canciones(playlist)

        elif opcion == 2:
            actualizar_populares(playlist)
            print("\nEstado de popularidad actualizado para todas las canciones.")

        elif opcion == 3:
            nombre_eliminar = input("\nIngrese el nombre de la canción que desea eliminar: ")
            indice = buscar_cancion(playlist, nombre_eliminar)
            
            if indice != -1:
                cancion_eliminada = playlist.pop(indice)
                print(f"La canción '{cancion_eliminada['nombre']}' ha sido eliminada de la playlist.")
            else:
                print(f"La canción '{nombre_eliminar}' no se encuentra en la playlist.")

        elif opcion == 4:
            nombre_buscar = input("\nIngrese el nombre de la canción a buscar: ")
            indice = buscar_cancion(playlist, nombre_buscar)
            
            if indice != -1:
                cancion = playlist[indice]
                estado = "POPULAR" if cancion["popular"] else "ESTÁNDAR"
                print(f"\nCanción encontrada en la posición {indice + 1}:")
                print(f"Nombre: {cancion['nombre']}")
                print(f"Duración (min): {cancion['minutos']}")
                print(f"Descargas: {cancion['descargas']}")
                print(f"Estado: {estado}")
            else:
                print(f"La canción '{nombre_buscar}' no se encuentra en la playlist.")

        elif opcion == 5:
            agregar_cancion(playlist)

        elif opcion == 6:
            print("\nGracias por usar el gestor de playlist. ¡Hasta luego!")


if __name__ == "__main__":
    main()