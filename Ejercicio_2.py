#Dado un numero decimal, determinar y mostrar la cantidad de dígitos enteros y decimales que tiene.

def ingresar_decimal():
    while True:
        try:
            numero_decimal = float(input("Ingrese un número decimal: "))
            return numero_decimal
        except ValueError:
            print("No ha ingresado un número decimal.")

def separar_decimal():
    numero_a_separar = ingresar_decimal()
    numero_a_string = str(numero_a_separar)
    numero_separado = numero_a_string.split('.')
    parte_entera = numero_separado[0]
    parte_decimal = numero_separado[1]
    return parte_entera, parte_decimal

def contar_enteros(numero_ingresado):
    parte_entera = numero_ingresado[0]
    return len(str(abs(int(parte_entera))))

def contar_decimales(numero_ingresado):
    parte_decimal = numero_ingresado[1]
    return len(parte_decimal) 

numero_ingresado = separar_decimal()

print("La cantidad de dígitos enteros es:" + str(contar_enteros(numero_ingresado)))

print("La cantidad de dígitos decimales es:" + str(contar_decimales(numero_ingresado)))