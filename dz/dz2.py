a = {'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 6500}}
a1 = input("какой словарь: ")
a2 = input("Что изменить: ")
a3 = int(input("На что изменить: "))
a[a1][a2] = a3
print(a[a1])