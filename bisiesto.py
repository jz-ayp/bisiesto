"""
Determinar si un año es bisiesto o no.
"""

# Entradas
anho = int(input("Introduzca el año: "))

# Proceso
if anho % 400 == 0 or anho % 4 == 0 and anho % 100 != 0:
    bisiesto = "sí"
else:
    bisiesto = "no"

# Salidas
print(f"El año {anho} {bisiesto} es bisiesto")
