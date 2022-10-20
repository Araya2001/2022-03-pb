# 1. - Alejandro
# Un hospital divide su trabajo en tres áreas: Ginecología, Pediatría y Cardiología. Desarrolle un programa que
# solicite al usuario un presupuesto anual y que calcule cuanto dinero recibe cada área
# según el presupuesto anual asignado
# ---
# Tres Áreas -> Ginecología (0.3), Pediatría (0.4) y Cardiología (0.3)
# Objetivos -> Solicitar al usuario un presupuesto anual, calcular cuanto dinero recibe cada área según el presupuesto
# anual (Dividido)
print("\n")
presupuesto_anual = float(input("Ingrese el presupuesto anual del hospital (Ingrese el monto en dólares):\n~ "))
print("El dinero que recibirá cada área será el siguiente: ")
str_format_float = "{:.2f}"
print("Ginecología:\t", str_format_float.format(presupuesto_anual * 0.3), "USD")
print("Pediatría:\t\t", str_format_float.format(presupuesto_anual * 0.4), "USD")
print("Cardiología:\t", str_format_float.format(presupuesto_anual * 0.3), "USD")
print("\n")

# 2. - Grupal
# Don Manrique adquirió una propiedad muy grande, la cual se encuentra dividida en varios lotes cuadrados.
# Escriba un programa que pida el valor del lado de un cuadrado
# y que muestre el valor del perímetro (en m) y del área (en m2) del cuadrado.
# ---
# Propiedad -> Dividido en lotes cuadrados
# Objetivo -> Apartir del lado de un cuadrado, mostrar el perímetro y el área del cuadrado
print("\n")
val_lado_cuadrado = float(input("Ingrese el lado del cuadrado (En metros):\n~ "))
perimetro = val_lado_cuadrado * 4
area = val_lado_cuadrado ** 2
print("El valor del perímetro es de:", perimetro, "m")
print("El valor del área es de:", area, "m²")
print("\n")

# 3. - Grupal
# El INS abrió un departamento de finanzas y estableció un programa para captar clientes: si el monto por el que
# se efectúa el préstamo es menor a $5000, deberá pagarse un 3% de interés sobre el monto, y si el monto es mayor
# o igual $5000, deberá pagarse un 2% de interés sobre el monto. Desarrolle una solución que pida el monto del préstamo
# y determine el monto de la cuota que se debe pagar.
# ---
# Prestamo < 5000 = 0.3
# Prestamo >= 5000 = 0.2

print("\n")
monto_add_interes = 0
monto_interes = 0
monto_a_solicitar = float(input("Ingrese el monto del préstamo (En dólares):\n~ "))
cant_meses_prestamo = int(
    input("Ingrese la cantidad de meses por el cuál se efectuara el préstamo (Mínimo 3 meses):\n~ "))
if cant_meses_prestamo <= 3:
    print("No ingresó una cantidad de meses válida")
else:
    if cant_meses_prestamo >= 5000:
        monto_add_interes = monto_a_solicitar * 1.2
        monto_interes = monto_a_solicitar * 0.2
    else:
        monto_add_interes = monto_a_solicitar * 1.3
        monto_interes = monto_a_solicitar * 0.3

    cuota = monto_add_interes / cant_meses_prestamo
    print("Cuota a pagar:", "{:.2f}".format(cuota))
    print("Total a pagar:", "{:.2f}".format(monto_add_interes))
    print("Total a intereses:", "{:.2f}".format(monto_interes))
    print("Cantidad de meses por el cuál se efectuará el prestamo:", cant_meses_prestamo)
print("\n")

# 4. - Lizeth
# El TSE requiere de un programa que solicite la edad de 5 personas e imprima cuantas de estas personas pueden votar.
# Considere que en Costa Rica para votar se requiere de tener al menos 18 años.
print("\n")
votar = 0
for i in range(5):
    edad = int(input("Digite su edad:\n~"))

    if edad >= 18:
        votar = votar + 1
print("La cantidad de personas a votar es de", votar)
print("\n")

# 5. - Isaí
# Utilizando una estructura de repetición, haga un programa que lea el precio de N productos (el sistema debe pedir
# hasta que el usuario no desee ingresar más datos), debe ir sumando el monto por cada artículo y al final imprimir
# el monto total a pagar. Antes debe aplicar el 13% por concepto de IVA.
print("\n")
produc = False
precio = 0

while produc == False:
    y_n = str(input("Desea agregar un producto y/n  "))

    if y_n.lower() == "n":
        produc = True
        break

    if y_n.lower() == "y":
        precio = precio + int(input("Digite el precio del pruducto: "))

print(precio * 1.13)
print("\n")
