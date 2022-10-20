salary = float(input("Digite su salario en dólares\n~ "))

if salary > 1000:
    salary = salary * 1.15
else:
    salary = salary * 1.20

str_salary = "{:.2f}".format(salary)
print("Su salario es:", str_salary)
