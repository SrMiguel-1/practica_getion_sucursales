import json
from sucursales import sucursales


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
    print("3. Volver")

    opcion = input("Seleccione una opción (1-3): ").strip()

    if opcion == "1":
        print("\n--- MODO EDICIÓN ---")
        print("(Deje el campo en blanco si no desae modificar)")

        nuevo_nombre = input(f"Nuevo Nombre [{sucursal_encontrada.get('nombre')}]: ").strip()
        nueva_direccion = input(f"Nueva dirección [{sucursal_encontrada.get('direccion')}]: ").strip()

        if nuevo_nombre:
            sucursales[indice_encontrado]["nombre"] = nuevo_nombre
        if nueva_direccion:
            sucursales[indice_encontrado]["direccion"] = nueva_direccion

        try:
            with open(ARCHIVOS_SUCURSALES, "w", encoding="utf-8") as archivo:
                json.dump(sucursales, archivo, indent=4, ensure_ascii=False)
            print("Sucursal editada y guardada exitosamente!!")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    elif opcion == "2":
        
        confirmacion = input(f"Estas seguro de eliminar la sucursal '{sucursal_encontrada.get('nombre')}'? (s/n): ").strip().lower()

        if confirmacion == 's':
            sucursales.pop(indice_encontrado)

            try:
                with open(ARCHIVOS_SUCURSALES, "w", encoding="utf-8") as archivo:
                    json.dump(sucursales, archivo, indent=4, ensure_ascii=False)
                print("Sucursal eliminada con éxito.")
            except Exception as e:
                print(f"Error al actualizar el archivo: {e}")

        else:
            print("Operación de eliminación cancelada.")

    elif opcion == "3":
        print("\nVolvinedo al menu principal...")
        return

    else:
        print("Opción inválida (1-3)")
        return


    





