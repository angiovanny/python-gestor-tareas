#!/usr/bin/env python3

import os

# Ruta portable
BASE_DIR = os.path.dirname(__file__)
FILENAME = os.path.join(BASE_DIR, "tareas.txt")


def inicializar_archivo():
    """
    Crea el archivo de tareas si no existe
    """
    if not os.path.exists(FILENAME):
        open(FILENAME, "w").close()


def cargar_tareas() -> list:
    """
    Carga tareas desde archivo

    Retorno:
        f.readlines() (list): Lista de tareas 
    """
    with open(FILENAME, "r") as f:
        return f.readlines()


def guardar_tareas(tareas: list):
    """
    Guarda todas las tareas en archivo

    Atributos:
        tareas (list): Lista de tareas
    """
    with open(FILENAME, "w") as f:
        f.writelines(tareas)


def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===\n")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")


def ver_tareas(tareas: list):
    """
    Muestra lista de tareas
    
    Atributos:
        tareas (str): Lista de tareas
    """
    if not tareas:
        print("\nNo hay tareas registradas.\n")
        return

    print("\nTareas:\n")

    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea.strip()}")


def agregar_tarea():
    """
    Agrega tarea a archivo
    """
    tarea = input("Escribe la tarea: ").strip()

    if not tarea:
        print("La tarea no puede estar vacía.")
        return

    with open(FILENAME, "a") as f:
        f.write(tarea + "\n")

    print("Tarea agregada correctamente.")


def eliminar_tarea(tareas: list):
    if not tareas:
        print("No hay tareas para eliminar.")
        return

    ver_tareas(tareas)

    try:
        num = int(input("Número de tarea a eliminar: "))

        if 1 <= num <= len(tareas):
            tareas.pop(num - 1)
            guardar_tareas(tareas)
            print("Tarea eliminada.")
        else:
            print("Número fuera de rango.")

    except ValueError:
        print("Debes ingresar un número válido.")


def main():
    inicializar_archivo()

    while True:
        tareas = cargar_tareas()

        mostrar_menu()

        opcion = input("Selecciona una opción: ").strip()

        match opcion:
            case "1":
                ver_tareas(tareas)

            case "2":
                agregar_tarea()

            case "3":
                eliminar_tarea(tareas)

            case "4":
                print("\nHasta luego 👋")
                break

            case _:
                print("Opción inválida.")


if __name__ == "__main__":
    main()