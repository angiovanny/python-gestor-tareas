from gestor.tareas import ver_tareas, agregar_tarea, eliminar_tarea

def test_ver_tareas_vacia():
    assert ver_tareas([]) == "\nNo hay tareas registradas.\n"

def test_ver_tareas_una():
    assert ver_tareas(["Leer un libro"]) == "\nTareas:\n1. Leer un libro\n"

def test_ver_tareas_varias():
    assert (ver_tareas(["Leer un libro", "Montar bici", "Estudiar Python", "Comprar mercado"]) == 
            "\nTareas:\n1. Leer un libro\n2. Montar bici\n3. Estudiar Python\n4. Comprar mercado\n")

def test_ver_tareas_espacios_tab():
    assert ver_tareas(["    Leer un libro  "]) == "\nTareas:\n1. Leer un libro\n"

def test_agregar_tarea_valida(monkeypatch, tmp_path):
    archivo = tmp_path / "tareas.txt" 

    monkeypatch.setattr(
        "gestor.tareas.FILENAME", archivo
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "Estudiar Python"
    )

    resultado = agregar_tarea()
    assert resultado == "Tarea agregada correctamente."
    
    with open(archivo, "r") as f:
        lineas = f.readlines()
    
    assert "Estudiar Python\n" in lineas

def test_agregar_tarea_vacia(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: ""
    )

    resultado = agregar_tarea()
    assert resultado == "La tarea no puede estar vacía."

def test_eliminar_tarea_vacia():
    assert eliminar_tarea([]) == "No hay tareas para eliminar."

def test_eliminar_tarea_invalida(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "abc"
    )

    tareas = ["A\n", "B\n"]

    resultado = eliminar_tarea(tareas)
    assert resultado == "Debes ingresar un número válido."

def test_eliminar_tarea_valida(monkeypatch, tmp_path):
    archivo = tmp_path / "tareas.txt" 

    monkeypatch.setattr(
        "gestor.tareas.FILENAME", archivo
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "2"
    )

    tareas = ["A\n", "B\n", "C\n"]

    resultado = eliminar_tarea(tareas)
    assert resultado == "Tarea eliminada."