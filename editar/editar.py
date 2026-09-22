import json
import os
import sucursales

ARCHIVOS_SUCURSALES= "data/data.json"

def editar_sucursal():
    try:
        with open(ARCHIVOS_SUCURSALES, "r", encoding="utf-8") as archivo:
                  sucursales = json.load(archivo)
    except FileNotFoundError:
        print("No se encontro archivo de sucursales.")
        sucursales = []
    except json.JSONDecodeError:
        print("El archivo JSON esta vacío o corrupto.")
        sucursales = []

    if not sucursales:
        print("No hay sucursales registradas actualmente.")
        return

    nombre = input("Ingrese el Nombre de la sucursal q desea buscar: ").strip().lower()

    sucursal_encontrada = None
    indice_encontrado = -1
    for indice, sucursal in enumerate(sucursales):
         id_actual = str(sucursal.get("id", "")).lower()
         nombre_actual = str(sucursal.get("nombre", "")).lower()

         if id_actual == nombre or nombre_actual == nombre:
            sucursal_encontrada = sucursal
            indice_encontrado = indice
            break

    if sucursal_encontrada is None:
        print(f"No se encontro ninguna sucursal con el nombre: '{nombre}'.")
        return

    print("\nSucursal encontrada")
    for clave, valor in sucursal_encontrada.items():
        print(f" - {clave.capitalize()}: {valor}")

    print("\nQue acción deseas realizar?")
    print("1. Editar datos")
    print("2. Eliminar sucursal")
    print("3. Cancelar")

    opcion = input("Seleccione una opción (1-3): ").strip()

    


