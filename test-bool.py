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
