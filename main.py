"""
Inserta el encabezado aquí y escribe tu código abajo


# Declaraciones
CONSTANTE = valor

# Entradas
entrada = input()

# Proceso


# Salidas
print(salida)
"""
# Entradas
anho = eval(input("Introduzca un año: "))
	
# Proceso
if anho % 100 == 0:
    # Año secular, tiene que ser divisible entre 400
    if anho % 400 == 0:
        resultado = "sí es"
    else:
        resultado = "no es"
else:
    # Año no secular, tiene que ser divisible entre 4
	if anho % 4 == 0:
		resultado = "es"
	else:
		resultado = "no es"
	
# Salidas
print("El año", anho, resultado, "bisiesto.")
