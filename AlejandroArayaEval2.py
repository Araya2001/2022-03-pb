# Estudio de Caso Práctico - Alejandro Araya

def is_even(grade):
    return grade % 2 == 0


def get_lowest_grade(grade, current_lowest_grade):
    scoped_number = grade
    if grade >= current_lowest_grade:
        scoped_number = current_lowest_grade
    return scoped_number


def get_highest_grade(grade, current_highest_grade):
    scoped_number = grade
    if grade <= current_highest_grade:
        scoped_number = current_highest_grade
    return scoped_number


def has_passed(grade):
    return grade >= 70


def is_between_limits(grade):
    return 0 <= grade <= 100


def read_student_agg():
    y_n_break_flag = False
    students_index = 0
    students_agg_message = "Desea agregar la nota final de un estudiante? ? [y/n]: "
    highest_grade = 0
    lowest_grade = 100
    even_grade_count = 0
    odd_grade_count = 0
    student_has_passed_count = 0
    student_has_not_passed_count = 0
    grade = 0
    while not y_n_break_flag:
        grade_break_flag = False
        if students_index != 0:
            students_agg_message = "Desea agregar la nota final de un estudiante adicional? [y/n]: "
        y_n = str(input(students_agg_message))
        if y_n.lower() == "n":
            y_n_break_flag = True
        if y_n.lower() == "y":
            while not grade_break_flag:
                grade = float(input("Ingrese la nota final del estudiante: "))
                grade_break_flag = is_between_limits(grade)
            highest_grade = get_highest_grade(grade, highest_grade)
            lowest_grade = get_lowest_grade(grade, lowest_grade)
            if is_even(grade):
                even_grade_count += 1
            else:
                odd_grade_count += 1
            if has_passed(grade):
                student_has_passed_count += 1
            else:
                student_has_not_passed_count += 1
            students_index += 1
        else:
            print("Por favor, ingrese una opción válida")
    print('\n------------------------------------------------------------------------------')
    print("Estudiantes qué han aprobado el curso:", student_has_passed_count)
    print("Estudiantes qué no han aprobado el curso:", student_has_not_passed_count)
    print("Nota más alta:", highest_grade)
    print("Nota más baja:", lowest_grade)
    print("Cantidad de notas pares:", even_grade_count)
    print("Cantidad de notas impares:", odd_grade_count)
    print('------------------------------------------------------------------------------')


read_student_agg()
