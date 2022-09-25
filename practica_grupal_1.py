# Los ejercicios realizados en este documento se encuentran alineados a la especificación de Python Enhancement
# Proposals (PEP)
# Referencia: https://peps.python.org/pep-0008/

# Constantes
CANTIDAD_SEMANAS_U = 15

# Realice un programa que dada la base y la altura de un rectángulo, calcule el área y el perímetro de este.
print("\nEjercicio 1:\n")
base = float(input("Ingrese la base del rectángulo (cm):\n~ "))
altura = float(input("Ingrese la altura del rectángulo (cm):\n~ "))
calc1 = base * altura
print("El área del rectángulo es de", calc1, "cm")
print("\nFinal ejercicio 1.")
print("\n---")

# Desarrolle un programa que solicite la distancia de su casa a la Universidad, el costo por kilómetro, la cantidad
# de días a la semana que viaja a la Universidad y que calcule el costo total de trasladarse por cuatrimestre.
# Asuma que cada visite implica ida y vuelta y que el cuatrimestre tiene 15 semanas.
print("\nEjercicio 2:\n")
distancia = float(input("Distancia de su casa a la Universidad (Km):\n~ "))
costo_x_kilometro = float(input("Costo por kilómetro del viaje (CRC):\n~ "))
cant_dias_viaje = int(input("Cantidad de dias que viaja a la Universidad:\n~ "))
calc2 = distancia * costo_x_kilometro * cant_dias_viaje * CANTIDAD_SEMANAS_U
print("El costo total de trasladarse por cuatrimestre es aproximadamente:", calc2, "CRC")
print("\nFinal ejercicio 2.")
print("\n---")

# Desarrolle un programa que solicite al usuario la edad de 5 personas y le muestre cuál es la edad promedio
