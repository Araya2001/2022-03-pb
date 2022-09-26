# Los ejercicios realizados en este documento se encuentran alineados a la especificación de Python Enhancement
# Proposals (PEP)
# Referencia: https://peps.python.org/pep-0008/

# Nombre de los integrantes de la práctica grupal:
# Alejandro Araya Jiménez
# Isai Badilla Martinez
# Sebastián Villalobos Mora
# Adrián Wong Bustos

# Constantes
CANTIDAD_SEMANAS_U = 15
CANTIDAD_SEMANAS_LABORALES = 4.2
CARGA_SOCIAL = 0.105
CARGA_SOLIDARIA = 0.05

# Realice un programa que dada la base y la altura de un rectángulo, calcule el área y el perímetro de este.
print("\nEjercicio 1:\n")
base = float(input("Ingrese la base del rectángulo (cm):\n~ "))
altura = float(input("Ingrese la altura del rectángulo (cm):\n~ "))
calc1 = base * altura
print("R/ El área del rectángulo es de", calc1, "cm")
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
print("R/ El costo total de trasladarse por cuatrimestre es aproximadamente:", calc2, "CRC")
print("\nFinal ejercicio 2.")
print("\n---")

# Desarrolle un programa que solicite al usuario la edad de 5 personas y le muestre cuál es la edad promedio
print("\nEjercicio 3:\n")
edad_persona1 = int(input("Introduzca la edad de la primera persona:\n~ "))
edad_persona2 = int(input("Introduzca la edad de la segunda persona:\n~ "))
edad_persona3 = int(input("Introduzca la edad de la tercera persona:\n~ "))
edad_persona4 = int(input("Introduzca la edad de la cuarta persona:\n~ "))
edad_persona5 = int(input("Introduzca la edad de la quinta persona:\n~ "))
calc3 = (edad_persona1 + edad_persona2 + edad_persona3 + edad_persona4 + edad_persona5) / 5
print("R/ La edad promedio es aproximadamente", calc3, "años")
print("\nFinal ejercicio 3.")
print("\n---")

# Desarrolle un programa que solicite al usuario la cantidad de horas semanales trabajadas, el precio que se le paga
# por hora y que calcule el salario mensual. Considere que se debe aplicar una deducción del 10.5% por cargas
# sociales y 5% por asociación solidarista. Asuma que cada mes cuenta con 4.2 semanas.
print("\nEjercicio 4:\n")
horas_x_semana = float(input("Introduzca la cantidad de horas que trabaja a la semana:\n~ "))
precio_x_hora = float(input("Introduzca el monto de lo que se le paga por hora (CRC):\n~ "))
salario_mensual_bruto = horas_x_semana * precio_x_hora * CANTIDAD_SEMANAS_LABORALES
salario_mensual_neto = salario_mensual_bruto - (salario_mensual_bruto * CARGA_SOCIAL) - \
                       (salario_mensual_bruto * CARGA_SOLIDARIA)
print("R/ El salario mensual con deducciones es aproximadamente de", salario_mensual_neto, "CRC")
print("\nFinal ejercicio 4.")
print("\n---")

# Desarrolle un programa que le solicite al usuario sus ingresos mensuales y sus gastos mensuales por alimentación.
# Con esta información el programa debe mostrar el porcentaje que gasto que corresponde al rubro de alimentación y
# el porcentaje que queda disponible para otros rubros.
print("\nEjercicio 5:\n")
ingreso_mensual = float(input("Introduzca sus ingresos mensuales (CRC):"))
gasto_alimento_mensual = float(input("Introduzca sus gastos en alimentación mensual (CRC):"))
porcentaje_alimento = (100 * gasto_alimento_mensual) / ingreso_mensual
porcentaje_restante = 100 - porcentaje_alimento
print("R/ El porcentaje de gastos de alimentación con respecto a los ingresos mensuales es del",
      str(porcentaje_alimento) + "%", "\nMientras tanto, el porcentaje de dichos ingresos disponible para otros "
                                      "rubros es del", str(porcentaje_restante) + "%.")
print("\nFinal ejercicio 5.")
print("\n---")
