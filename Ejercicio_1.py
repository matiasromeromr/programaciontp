def ingreso_numero_entero():
    while True:
        try:
            numero_entero = int(input("Ingrese un número entero: "))
            return numero_entero 
        except ValueError:
            print("No ha ingresado un número entero.") 


def contador_digitos(numero_ingresado):
    cantidad_digitos = len(str(abs(numero_ingresado)))
    return cantidad_digitos


numero = ingreso_numero_entero() 

cantidad = contador_digitos(numero) 

print(f"El número que hay ingresado tiene {cantidad} dígitos.") 