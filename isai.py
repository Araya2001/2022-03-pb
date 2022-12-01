# Examne Isai Badilla

def notas():
    aprobados = 0
    reprobados = 0
    pares = 0
    impares = 0
    nota_alta = 0
    nota_baja = 100

    entrada_usuario = 1

    while entrada_usuario != -1:
        entrada_usuario = int(input("Ingrese las notas o ingrese -1 para terminar: "))
        if entrada_usuario != -1 and (0 <= entrada_usuario <= 100):
            nota = entrada_usuario
            if nota >= 70:
                aprobados = aprobados + 1
            else:
                reprobados = reprobados + 1

            if nota % 2 == 0:
                pares = pares + 1
            else:
                impares = impares + 1

            if nota >= nota_baja:
                nota_baja = nota_baja
            else:
                nota_baja = nota

            if nota <= nota_alta:
                nota_alta = nota_alta
            else:
                nota_alta = nota
        elif not (0 <= entrada_usuario <= 100):
            if entrada_usuario != -1:
                print("Opción incorrecta!")
    print("El total de alumnos aprobados fueron: ", aprobados)
    print("El total de alumnos reprobados fueron: ", reprobados)

    print("Las notas pares son: ", pares)
    print("Las notas impares son: ", impares)

    print("La nota mas alta es: ", nota_alta)
    print("La nota mas baja es: ", nota_baja)


notas()
