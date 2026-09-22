import json

def listar_sucursales():
    with open("sucursales.json", "r", encoding="utf-8") as archivo:
        sucursales = json.load(archivo)

    print("------ LISTA DE SUCURSALES -------------")
    

    for sucursal in sucursales:
        print("--------------------------")
        print("Nombre:", sucursal["nombre"])
        print("Dirección:", sucursal["direccion"])
        print("Teléfono:", sucursal["telefono"])
        print("Gerente:", sucursal["gerente"])
        print("Estado:", sucursal["estado"])


print("---------resultado---------")
listar_sucursales()
print("---------fin del listado---------")