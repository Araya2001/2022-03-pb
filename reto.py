# Enunciado:
# Utilizando una estructura de repetición, haga un programa que lea el precio de N  productos (el sistema debe pedir
# hasta que el usuario no desee ingresar más datos), debe ir sumando el monto por cada articulo y al final imprimir el
# monto total a pagar. Antes debe aplicar el 13% por concepto de IVA.
#
# Realizar ejercicio y subir archivo .py con la solucion. El integrnate que lo suba mas rapido y de manera correcta
# ganara la actividad y el gane para su grupo.

sum_total = 0.0
is_finished = False

print("Ingrese una lista de productos: \n")
while not is_finished:
    input_y_n = str(input("Desea agregar un producto? (y/n):"))
    if input_y_n.lower() == "y":
        sum_total += (float(input("Ingrese el monto en colones de dicho producto: ")) * 1.13)

    if input_y_n.lower() == "n":
        is_finished = True

print(sum_total)
