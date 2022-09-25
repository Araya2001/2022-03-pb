# Los ejercicios realizados en este documento se encuentran alineados a la especificación de Python Enhancement
# Proposals (PEP)
# Referencia: https://peps.python.org/pep-0008/

# Realice un programa que dada la base y la altura de un rectángulo, calcule el área y el perímetro de este.

print("Ejercicio 1)")
base = float(input("Ingrese la base del rectángulo:"))
altura = float(input("Ingrese la altura del rectángulo:"))
calc = base * altura
print("El área del rectángulo es:", calc)

# Desarrolle un programa que solicite la distancia de su casa a la Universidad, el costo por kilómetro, la cantidad
# de días a la semana que viaja a la Universidad y que calcule el costo total de trasladarse por cuatrimestre.
# Asuma que cada visite implica ida y vuelta y que el cuatrimestre tiene 15 semanas.
print("Ejercicio 2)")
distancia = float(input("Distancia de su casa a la Universidad:"))
costo_x_kilometro = float(input("Costo por kilómetro del viaje:"))
cant_dias_viaje = int(input("Cantidad de dias que viaja a la Universidad:"))
cant_semanas