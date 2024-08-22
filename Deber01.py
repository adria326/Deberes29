# Lista para almacenar los estudiantes y sus calificaciones
estudiantes = []

# Función para agregar un estudiante
def agregar_estudiante(nombre, calificaciones):
    estudiantes.append({"nombre": nombre, "calificaciones": calificaciones})
    print(f"Estudiante '{nombre}' agregado.")

# Función para mostrar la lista de estudiantes numerada
def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes en la lista.")
    else:
        print("Lista de estudiantes:")
        for i, estudiante in enumerate(estudiantes, start=1):
            print(f"{i}. {estudiante['nombre']}")

# Función para actualizar las calificaciones de un estudiante
def actualizar_estudiante():
    if not estudiantes:
        print("No hay estudiantes para actualizar.")
        return

    mostrar_estudiantes()
    try:
        seleccion = int(input("Elige el número del estudiante que deseas actualizar: ")) - 1
        if seleccion < 0 or seleccion >= len(estudiantes):
            print("Selección no válida.")
            return

        nuevo_nombre = input(f"Ingresa el nuevo nombre para '{estudiantes[seleccion]['nombre']}' (o presiona Enter para no cambiarlo): ").strip()
        nuevas_calificaciones = input("Ingresa las nuevas calificaciones separadas por comas: ").split(',')

        if nuevo_nombre:
            estudiantes[seleccion]['nombre'] = nuevo_nombre

        estudiantes[seleccion]['calificaciones'] = [float(nota.strip()) for nota in nuevas_calificaciones]
        print("Estudiante actualizado.")
    except ValueError:
        print("Entrada no válida.")

# Función para eliminar un estudiante
def eliminar_estudiante():
    if not estudiantes:
        print("No hay estudiantes para eliminar.")
        return

    mostrar_estudiantes()
    try:
        seleccion = int(input("Elige el número del estudiante que deseas eliminar: ")) - 1
        if seleccion < 0 or seleccion >= len(estudiantes):
            print("Selección no válida.")
            return

        estudiante_eliminado = estudiantes.pop(seleccion)
        print(f"Estudiante '{estudiante_eliminado['nombre']}' eliminado.")
    except ValueError:
        print("Entrada no válida.")

# Función principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Ingresa el nombre del estudiante: ").strip()
            calificaciones = input("Ingresa las calificaciones separadas por comas: ").split(',')
            calificaciones = [float(nota.strip()) for nota in calificaciones]
            agregar_estudiante(nombre, calificaciones)
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            actualizar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

# Llamada a la función principal
main()