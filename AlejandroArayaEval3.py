# Estudio de Caso Práctico - Alejandro Araya
# Sección 3

import random
from datetime import datetime

row_qty = 7
col_qty = 7


def file_writter_append(section, result):
    file = open("result.txt", "a")
    file.write(str(datetime.now().isoformat()) + " - resultado - " + section + " :\t" + result + "\n")
    file.close()


def init_mtx():
    mtx = []
    for i in range(0, col_qty):
        mtx.append([])
        for j in range(0, row_qty):
            random.seed(datetime.now().timestamp())
            val = random.randint(0, 9999999)
            mtx[i].append(val)
    return mtx


# for x in mtx_of_numbers:
#     print(x)


def do_print(mtx):
    str_header = "\t|"
    str_sequence_column = []
    str_val_column = []
    for i in range(0, col_qty):
        str_header += "\t\t" + str(i + 1) + "\t\t|"
    for row in range(0, row_qty):
        str_sequence_column.append(str(row + 1) + "\t|")
    for row in range(0, row_qty):
        str_val_column.append([])
        for col in range(0, col_qty):
            str_val_column[row].append("\t" + str(mtx[row][col]) + "\t\t|")
    print(str_header)
    for row in range(0, row_qty):
        str_line = str_sequence_column[row]
        for col in range(0, col_qty):
            str_line += str_val_column[row][col]
        print(str_line)
    print("\n")


def sum_specific_mtx_row(row_num, mtx):
    sum_of_row = 0
    for col in mtx[row_num]:
        sum_of_row += col
    return sum_of_row


def sum_specific_mtx_col(col_num, mtx):
    sum_of_col = 0
    for col in mtx:
        sum_of_col += col[col_num]
    return sum_of_col


def get_total_of_even_numbers(mtx):
    total = 0
    for row in mtx:
        for col in row:
            if col % 2 == 0:
                total += 1
    return total


def get_total_of_odd_numbers(mtx):
    total = 0
    for row in mtx:
        for col in row:
            if not (col % 2 == 0):
                total += 1
    return total


def request_data_and_save():
    mtx_of_numbers = init_mtx()
    print("A continuación, la siguiente matriz de números:\n")
    do_print(mtx_of_numbers)
    row_selection = int(input("Por favor seleccione una fila, del 1 al 7,  para realizar la sumatoria de esta: "))
    col_selection = int(input("Por favor seleccione una columna, del 1 al 7,  para realizar la sumatoria de esta: "))
    if not (0 > row_selection > row_qty):
        value = sum_specific_mtx_row(row_selection - 1, mtx_of_numbers)
        file_writter_append("sumatoria de fila " + str(row_selection), str(value))
        print("sumatoria de fila " + str(row_selection), str(value))
    else:
        print("El número de fila ingresado no es un valor correcto.")
    if not (0 > col_selection > col_qty):
        value = sum_specific_mtx_col(col_selection - 1, mtx_of_numbers)
        file_writter_append("sumatoria de columna " + str(col_selection), str(value))
        print("sumatoria de columna " + str(col_selection), str(value))
    else:
        print("El número de columna ingresado no es un valor correcto.")
    total_even_numbers = get_total_of_even_numbers(mtx_of_numbers)
    total_odd_numbers = get_total_of_odd_numbers(mtx_of_numbers)
    file_writter_append("total de números pares en la matriz", str(total_even_numbers))
    file_writter_append("total de números impares en la matriz", str(total_odd_numbers))
    print("total de números pares en la matriz", str(total_even_numbers))
    print("total de números impares en la matriz", str(total_odd_numbers))


request_data_and_save()
