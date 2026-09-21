import json
DATOS = "practica_getion_sucursales/data/data.json"

def guardar_datos(datos):
    with open(DATOS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def registrar_sucursal():
    
    print("Vamos a registrar una sucursal")
    
    nombre = input("Ingresa el nombre de la sucursal")
    direccion = input("Ingresa la dirección de la sucursal")
    
    id_gerente = int(input("Ingrese el id del gerente"))
    try:
        telefono = int(input("Ingrese el telefono"))
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")
    

    datos = {"Nombre_sucursal":nombre,
             "Direccion_sucursal": direccion,
             "id_gerente":id_gerente,
             "telefono":telefono}
    guardar_datos(datos)
    