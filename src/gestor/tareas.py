#!/usr/bin/env python3

import os

# Ruta portable
BASE_DIR = os.path.dirname(__file__)
FILENAME = os.path.join(BASE_DIR, "tareas.txt")
from context import managed_file
from decorators import log_execution

@log_execution
def inicializar_archivo():
    """
    Crea el archivo de tareas si no existe

    Example:
        >>> inicializar_archivo()
    """
    if not os.path.exists(FILENAME):
        managed_file(FILENAME, "w").close()

@log_execution
def cargar_tareas() -> list:
    """
    Carga tareas desde archivo

    Returns:
        (list): Lista de tareas 

    Example:
        >>> cargar_tareas()
    """
    with managed_file(FILENAME, "r") as f:
        return f.readlines()

@log_execution
def guardar_tareas(tareas: list):
    """
    Guarda todas las tareas en archivo

    Args:
        tareas (list): Lista de tareas

    Example:
        >>> guardar_tareas(["Leer libro", "Hacer ejercicio"])
    """
    with managed_file(FILENAME, "w") as f:
        f.writelines(tareas)

def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===\n")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

@log_execution
def ver_tareas(tareas: list) -> str:
    """
    Formatea lista de tareas para mostrar
    
    Args:
        tareas (str): Lista de tareas

    Returns:
        String formateado con las tareas

    Example:
        >>> ver_tareas(["Leer libro", "Hacer ejercicio"])
    """
    if not tareas:
        return "\nNo hay tareas registradas.\n"

    resultado = "\nTareas:\n"

    for i, tarea in enumerate(tareas, start=1):
        resultado += f"{i}. {tarea.strip()}\n"

    return resultado
        
@log_execution
def agregar_tarea() -> str:
    """
    Agrega tarea a archivo

    Returns:
        (str): String formateado con resultado

    Example:
        >>> agregar_tarea()
    """
    tarea = input("Escribe la tarea: ").strip()

    if not tarea:
        return "La tarea no puede estar vacía."

    with managed_file(FILENAME, "a") as f:
        f.write(tarea + "\n")

    return "Tarea agregada correctamente."

@log_execution
def eliminar_tarea(tareas: list) -> str:
    """
    Elimina tareas de lista

    Args:
        tareas (str): Lista de tareas

    Returns:
        (str): String formateado con resultado

    Example:
        >>> eliminar_tareas(["Leer libro", "Hacer ejercicio"])
    """
    if not tareas:
        return "No hay tareas para eliminar."

    print(ver_tareas(tareas))

    try:
        num = int(input("Número de tarea a eliminar: "))

        if 1 <= num <= len(tareas):
            tareas.pop(num - 1)
            guardar_tareas(tareas)
            return "Tarea eliminada."
        else:
            return "Número fuera de rango."

    except ValueError:
        return "Debes ingresar un número válido."


def main():
    inicializar_archivo()

    while True:
        tareas = cargar_tareas()

        mostrar_menu()

        opcion = input("Selecciona una opción: ").strip()

        match opcion:
            case "1":
                print(ver_tareas(tareas))

            case "2":
                print(agregar_tarea())

            case "3":
                print(eliminar_tarea(tareas))

            case "4":
                print("\nHasta luego 👋")
                break

            case _:
                print("Opción inválida.")


if __name__ == "__main__":
    main()