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
        sucursales=[]
    except
