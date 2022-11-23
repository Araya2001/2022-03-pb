# Notas:
# Minor es taxista
# Días que labora: 6 (Lun-Sab)
# Taxi es alquilado -> Pago de tarifa
# Km X Día -> Alquiler
# Si es superior a 100 KM = 25000
# Si es inferior a 100 KM = 20000
# Llevar registro de estp

sum_rent_total = 0
sum_km_total = 0
days_per_km = [
    ['Lunes', 0, 0],
    ['Martes', 0, 0],
    ['Miércoles', 0, 0],
    ['Jueves', 0, 0],
    ['Viernes', 0, 0],
    ['Sábado', 0, 0]
]

day_index = 0
km_index = 1
rent_index = 2

# Parte 1 - Lógica
for day in days_per_km:
    break_flag = False
    km_on_day = 0
    while break_flag == False:
        y_n = str(input("Desea agregar kilometraje para el día " + day[day_index] + "? y/n: "))
        if y_n.lower() == "n":
            break_flag = True
        if y_n.lower() == "y":
            km_on_day += int(input('Ingrese la cantidad de kilómetros que registro el día ' + day[day_index] + ' : '))
    day[km_index] = km_on_day
    if km_on_day >= 100:
        day[rent_index] = 25000
    else:
        day[rent_index] = 20000
    sum_rent_total += day[rent_index]
    sum_km_total += day[km_index]

# Parte 2 - Mostrar datos de interés
print('Datos Semanales Minor - Taxi:')
for day in days_per_km:
    print('\n')
    print('Kilometraje del día', day[day_index], ':', day[km_index], )
    print('Costo del alquiler del día', day[day_index], ':', day[rent_index])

print('\n')
print('Total de kilómetros recorridos por Minor :', sum_km_total)
print('Total de alquiler que debe pagar Minor :', sum_rent_total)

# Parte 3 - Mostrar arreglo con día y kilómetro
print('\n')
print('Arreglo:')
for x in days_per_km:
    print(x[day_index], ':', x[km_index])
