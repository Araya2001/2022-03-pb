# Los ejercicios realizados en este documento se encuentran alineados a la especificación de Python Enhancement
# Proposals (PEP)
# Referencia: https://peps.python.org/pep-0008/

# 1.
# Elaborar un programa que muestre un mensaje de bienvenida para una persona.
# Debe imprimir la información como se muestra a continuación:
# Bienvenido, estimado Nombre PrimerApellido SegundoApellido. -> primer_apellido, segundo_apellido
# print("\nEjercicio 1:\n")
# nombre = str(input("Ingrese su nombre:\n~ "))
# primer_apellido = str(input("Ingrese su primer apellido:\n~ "))
# segundo_apellido = str(input("Ingrese su segundo apellido:\n~ "))
# print("Bienvenido, estimado", nombre, primer_apellido, segundo_apellido + ".")
# print("\nFinal ejercicio 1.")
# print("\n---")

# 2.
# ¡Vamos a crear una especie de calculadora simple! El programa calculará el de la suma, la resta,
# la multiplicación y la división de dos números y mostrará los resultados obtenidos.
#
# TODO: Nota - Considere que, si ingresamos un cero como segundo valor, obtendremos un error durante la ejecución del
# TODO: programa. En próximas lecciones veremos cómo controlar este error.
print("\nEjercicio 2:\n")
print("Nota: Respetar los espacios a como se encuentra definido en los ejemplos\n")
str_calc = str(
    input("Ingrese una expresión matemática que desee calcular\nEj:\n-> 1 + 2\n-> 2 - 1\n-> 2 * 5\n-> 4 / 2\n...\n~ ")
)
# 1 + 2
# 1, espacio, +, espacio, 2
# split ? -> pasa por argumento el caracter o cadena de caracteres por el que se desea separar.
# split -> retorna una matriz con los campos que no son el argumento especificado.
# [1, +, 2]
# arreglo[0] = 1
# arreglo[1] = +
# arreglo[2] = 2
str_calc_arr = str_calc.split(" ")
calc = 0

if len(str_calc_arr) == 3:
    num1 = int(str_calc_arr[0])
    operator = str_calc_arr[1]
    num2 = int(str_calc_arr[2])
    if operator == "+":
        calc = num1 + num2
    elif operator == "-":
        calc = num1 - num2
    elif operator == "*":
        calc = num1 * num2
    elif operator == "/":
        calc = num1 / num2
    else:
        print("Ingrese una expresión valida")
    format_expression = "{:.2f}"
    print(str_calc, "=", format_expression.format(calc))
    print("Suma:", num1 + num2)
    print("Resta:", num1 - num2)
    print("Multiplicación:", num1 * num2)
    print("División:", num1 / num2)
else:
    print("Ingrese una expresión valida")

print("\nFinal ejercicio 2.")
print("\n---")

# 3.
# Elabore un programa que calcule y muestre el área y el perímetro de un cuadrado.
#
# TODO: Nota - Para realizar los cálculos requiere conocer la medida del lado del cuadrado.
print("\nEjercicio 3:\n")
lado = float(input("Ingrese el lado del cuadrado (cm):\n~ "))
area = lado ** 2
perimetro = lado * 4
print("El área del cuadrado es de", area, "cm y el perímetro de este es de", perimetro, "cm")
print("\nFinal ejercicio 3.")
print("\n---")

# 4.
# Desarrolle un programa intercambie el valor de las edades de Luis y Pedro y muestre las edades luego de
# realizado el intercambio.
#
# TODO: Nota - Considere que las variables solo pueden almacenar un valor a la vez, por lo que el asignar un nuevo valor
# TODO: provocará la pérdida del valor anterior.
print("\nEjercicio 4:\n")
edad_luis = int(input("Ingrese la edad de Luis:\n~ "))
edad_pedro = int(input("Ingrese la edad de Pedro:\n~ "))
temp_edad_luis = edad_luis
edad_luis = edad_pedro
edad_pedro = temp_edad_luis
print("Las edades intercambiadas serían las siguientes:\nLuis:", edad_luis, "\nPedro:", edad_pedro)
print("\nFinal ejercicio 4.")
print("\n---")
# 5.
# Desarrolle un programa que eleve un número a una potencia.
#
# TODO: Nota - Debe utilizar instrucciones de lectura y operaciones aritméticas.
print("\nEjercicio 5:\n")
int_base = float(input("Ingrese un número (base)\n~ "))
int_exponent = int(input("Ingrese otro número (exponente)\n~ "))
calc_exp = int_base ** int_exponent
print("El número", int_base, "elevado a la potencia", int_exponent, "es", calc_exp)
print("\nFinal ejercicio 5.")
print("\n---")
