from sucursales import sucursales


print("Bienvenidos a el programa")

while True:
    print("Menu")
    print("1. Registrar sucursales")
    print("2. Editar sucursales")
    print("3. Eliminar sucursales")
    print("4. Salir")
    try:
        
        n_sucursal = int(input("Ingresa el número correspondiente "))

        if n_sucursal == 1:
            print("registro")
            sucursales.registrar_sucursal()
        elif n_sucursal == 2:
            #funcion editar  sucursal
            print("editar")
        elif n_sucursal == 3:
            #funcion eliminar sucursales
            print("eliminar")
        elif n_sucursal == 4:
            #Salir
            break
        else:
            print("Valor no válido")
    except ValueError:
            print("Error: Debes ingresar un número entero válido.")
