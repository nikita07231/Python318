# name = "Nikolay"
# print("Hello,", name, "!")

# a = 30
# b = "Hello"
# c = 2.8
# print(type(c))
# print(type(a))
# print(type(b))

# number = (6 + 4) * (5 ** 2 +7)
# print(number) #320

# num = 10
# num += 5
# print(num)
#
# num -=3
# print(num)

# num = 4321
# a = num % 10
# b = num % 100 // 10
# c = num % 100 // 100
# d = num // 1000
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# print(num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# print(int(2.5))
# print(round(2.51))
# print(round(2.519, 2))

# a = 2.519
# b = round(a)
# print(b, type(b))
# c = round(a, 2)
# print(c, type(c))

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут" , name + ". Мне", age, "лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="--", end=" $$ ")
# print("Hello")

# name = input("Введите имя: ")
# print("Hello,", name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
#
# res = num ** power
# print(res)

# a = int(input("Первое число: "))
# b = int(input("Второе число: "))
# c = int(input("Третье число: "))
# d = int(input("Четвёртое число: "))
# res1 = a + b
# res2 = c + d
# res = res1/res2
# print(round(res, 2))

# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)

# print(bool("python"))
# print(bool(""))
# print(bool(" "))
# print(bool("4564"))

# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10 - 3)
# print("привет" > "ПРИВЕТ")

# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print( 3* 3 <= 7 >= 2)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)
# print(5 - 3 == 2 and 1 + 3 < 4)
# print(5 - 3 > 2 and 1 + 3 == 4)
# print(5 - 3 > 2 and 1 + 3 > 4)

# print(5 - 3 == 2 or 1 + 3 == 4)
# print(5 - 3 == 2 or 1 + 3 < 4)
# print(5 - 3 > 2 or 1 + 3 == 4)
# print(5 - 3 > 2 or 1 + 3 > 4)

# print(not 9 - 5)
# print(not 9 - 9)

# cnt = 15
# if cnt < 10:
#     cnt += 1
#     print(cnt)

# age = int(input("Введите свой возраст"))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 25
# b = 25
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a=b")

# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
# if a == b == c:
#     print("Равносторонний")
# elif a == b or a == c or b == c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# day = int(input("Введите день недели цифрой: "))
# if 1 <= day <= 5:
#     print("Рабочий день", end=" ")
#     if day == 1:
#         print("понедельник", end=" ")
#     elif day == 2:
#         print("вторник")
#     elif day == 3:
#         print("среда")
#     elif day == 4:
#         print("четверг")
#     else:
#         print("пятница")
# elif 6 <= day <=7:
#     print("выходной день")
#     if day == 6:
#         print("суббота")
#     else:
#         print("воскресенье")
# else:
#     print("Ошибка")

# day = int(input("Введите месяц года: "))
# if 3 <= day <= 5:
#     print("Весна")
# elif 6<= day <= 8:
#     print("Лето")
# elif 9 <= day <= 11:
#     print("Осень")
# elif day == 12 or 1<=day <=2 :
#     print("Зима")
# else:
#     print("Ошибка ввода")

# n = int(input("Введите кол-во ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# password = "admin"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Такого значения не существует")

# day = "Понедельник"
# time = 17
#
# match day:
#     case "Понедельник" | "вторник" | "Среда" | "Четверг" | "Пятница" if 9 <= time <= 16:
#         print("рабочей день")
#     case "Суббота" | "Воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")

# a, b, = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 20, 30
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# chis, deli = 2, 0
# print(chis/deli if deli != 0 else "На ноль делить нельзя")

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError , ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на ноль")
# else: # отработает когда в блоке try не возникло исключений
#     print("Всё нормально. Вы ввели числа", n, "и", m)
# finally: # отработает в любом случии
#     print("Конец программы")
# a = (input("Ведите первое число"))
# b = (input("Ведите второе число"))
# try:
#     print(int(a) + int(b))
# except ValueError:
#     print(a+b)

# Циклы

# i = 10
# while i > 0:
#     print("i =",i)
#     i -= 2

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# n = int(input("Введите кол-во *"))
# i = 1
# while i <= n:
#     print("*")
#     i += 1

# while n > 0:
#     print("*")
#     n -= 1

# nac = int(input("Введите начало диапазона: "))
# kon = int(input("Введите конец диапазона: "))
# sum = 0
# i = nac
# while nac <= i <= kon:
#     if i % 2 != 0:
#         sum += i
#     i += 1
# print("Сумма нечетных чисел:", sum)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# res = 1
# while True:
#     a = int(input("Введите число"))
#     if a == 0:
#         break
#     res *= a
# print("Результат:", res)

# i = 0
# while i < 10:
#     # if i == 5:
#     #     break
#     if i == 8:
#         print(5/0)
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)
# j = 1
# i = 1
# while i <5:
#     print("Внешний цикл: i = ", i)
#
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j+=1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*",j,"=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1
# print()
# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1

# for element in collection:
#    print(element)

# for i in "Hello!":
#     print(i)
#
# for color in "red", "blue", "green":
#     print(color)

# print(range(9))
# # range(start, stop, step)
#
# for i in range(9):
#     print(i, end=" ")
#
# print()
#
# i = 0
# while i < 9:
#     print(i, end=" ")
#     i += 1

# a = int(input("Введите целое число"))
# for i in range(1,a):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10,100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Конец цикла")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("----")

# w = int(input("Введите ширину прямоугольника"))
# h = int(input("Введите высоту прямоугольника"))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# d = [i for i in "Hellow"]
# print(d)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# nums = [8, 3, 9, 4, 1, "Hello", True]
# # print(nums)
# # print(type(nums))
# # print(nums[0])
# # print(nums[-1])
# nums[1] = 256
# nums[2] += 100
# print(nums)
# # for i in nums:
# #     print(i)
# print(len(nums))
# s = [1, 3, 5]
# print(s)
# print(type(s))
#
# s1 = list("Hello")
# print(s1)
# print(type(s1))
#
# s2 = s1 + s
# print(s2)
#
# s3 = s * 2
# print(s3)

# n = list(range(2, 10, 3))
# print(n)
# a = [0 for i in range(5)]
# print(a)
#
# a1 = [i**2 for i in range(1, 25)]
# print(a1)
#
# a2 = [i * 3 for i in "Python"]
# print(a2)

# a = [0] * int(input("Введите кол-во элементов списка"))
# print(a)
#
# for i in range(len(a)):
#     a[i] = int(input("->"))
# print(a)

# sum = 0
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# for i in a:
#     if i < 0:
#         sum += i
# print(sum)

# s = list(range(10, 100, 10))
# print(s)
#
# for i in range(len(s)):
#     print(s[i], end=" ")
# print()
# for i in s:
#     print(i, end=" ")
# count = sum2 = 0
# n = list(range(21,41))
# print(n)
# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         sum2 += i
# print(count)
# print(sum2)

# n = [int(input("->")) for i in range(int(input("n = ")))]
# print(n)
#
# for i in range(len(n)-1):
#     if n[i] < n[i+1]:
#         print(n[i+1], end=" ")
# sum = count = 0
# n = [int(input("->")) for i in range(int(input("n = ")))]
# for i in n:
#     if i != 0:
#         count += 1
#         sum += i
# print("Среднее арифметическое: ", sum/count )

# a = [7, 9, 2, 1, 17]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

# Срез = список[start:stop:step]
# s = [5, 9, 3, 7, 1, 8]
# print(s)
# print(s[1:3])

# lst = list(range(1,8))
# print(lst[:])
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[6:])
# print(lst[3:4])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# st = "Hello"
# print(st)
# print(st[::-1])

# методы списков dir(list)
# s = [9, 5, 6, 3, 7, 4]
# print(s)
# s.append(8) # добавили элемент в конец списка
# s.append("add")
# print(s)
# s.extend([20, 1, 2]) # добавили набор элементов в конец списка
# s.extend("add")
# print(s)
# s.insert(0,100) # добавляет элемент (второй параметр) по заданному индексу (первый элемент)
# s.insert(-1, 222)
# print(s)

# s = []
# n = int(input("Введите кол-во элементов списка:"))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x,"не делится на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
#
# s = []
# for el in a:
#     if el in b and el not in s:
#         s.append(el)
# print(s)

# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# a = [7, 9, 2, 9, 1, 17, 9]
# print(a)
# # a.remove(9) # удаляет элемент по значению
# # print(a)
# # last = a.pop() # удаляет последний элемент из списка и возвращает удалённый элемент
# # print(last)
# # print(a)
# # second = a.pop(0)
# # print(second) # удаляет элемент по индексу
# # print(a)
# # a.clear() # очищает список
# # print(a)
# # num = a.count(9) # считает кол-во заданных значений в списке
# # print(num)
# # ind = a.index(17) # возвращает индекс элемента по заданному значению
# # print(ind)
# # ind2 = a.index(9,2)
# # print(ind2)
#
# # num = 7
# # if num in a:
# #     print(a.index(num))
# a.reverse()
# print(a)

# a = [1, 2, 3]
# b = a.copy()
# print("a =", a)
# print("b =", b)
# a.append(4)
# print("a =", a)
# print("b =", b)

# a = [7, 9, 2, 9, 1, 17, 9]
# print(a)
# # a.sort() # сортировка элементов по возрастанию
# a.sort(reverse=True)
# print(a)

# s = ["Виталий", "Сергей", "Александр", "Анна"]
# print(s)
# s.sort(key=len, reverse=True)
# print(s)
# print(len(s))
# print(len(s[0]))

# lst = sorted(s, key=len, reverse=True)
# print(lst)
# print(s)

# Генерация случайных данных

# import random

# print(random.random())
# print(random.randint(0, 9))
# print(random.randrange(3, 9, 2))
#
# print(round(random.uniform(10.5, 25.5), 2))
# s = [20, 30, 40, 50, 60, 70, 80, 90, 10]
# print(s)
# # random.shuffle(s)
# print(random.choice(s,))
# print(random.choices(s, k=3))

# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)

# s = ['20', '30', '40', '50', '60', '70', '80', '90', '10']
# print(s)
# print(len(s))
# print(sum(s))
# print(max(s))
# print(min(s))

# A = [random.randint(0,100) for x in range(10)]
# print(A)
# max = max(A)
# print(max)
# A.remove(max)
# A.insert(0,max)
# print(A)

# x = list('1725gfa')
# print(x)
# print('a' not in x)
# s = 'c'
# if s in x:
#     print('Такой элемент в списке есть')
# else:
#     print(s, "В списке отсутствует")

# lst = []
# if not lst:
#     print("Список пустой")
#
# print(bool(lst))

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список: ",a)
# print("Второй список", b)
# c = a + b
# print(c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print(c)

# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print(c)

# c = [min(a), min(b), max(a), max(b)]
# print(c)

# n1 = int(input("Размер списка"))
# # a = [random.randint(0,10) for i in range(n1)]
# a = []
# while len(a) != n1:
#     n = random.randrange(n1)
#     if n not in a:
#         a.append(n)
# print(a)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m, end="\n\n")
# # print(m[1][2])
#
# # s = ["Hello", "world"]
# # print(s[1][0])
# for row in range(len(m)):  # 0 1 2
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#     print()
#
# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# for row in m:
#     for x in row:
#         print(x**2, end="\t\t")
#     print()

# w, h = 5, 3
# matrix = [[random.randint(1, 20)for x in range(w)]for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# for x, y in [[1,  2], [3, 4], [5, 6], [7, 8]]:
#     print(x,"+", y, "=", x + y)

# import math
#
# num1 = math.sqrt(4)
# num2 = math.pi
# num3 = math.ceil(3.2)
#
# print(num1)
# print(num2)
# print(num3)

# import math as m
#
#
# num3 = m.ceil(3.2)
# num4 = m.floor(3.8)
#
# print(num3)
# print(num4)

# from math import *
#
#
# num3 = ceil(3.2)
# num4 = floor(3.8)
#
# print(num3)
# print(num4)

# from math import ceil as c, floor as f
#
#
# num3 = c(3.2)
# num4 = f(3.8)
#
# print(num3)
# print(num4)

# from math import pi
#
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности: ", round(2 * pi * radius, 2))

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")

# second = time.time()
# print(second)
# s = 1550704510
# local_time = time.ctime()
# print(local_time)
#
# res = time.localtime()
# print(res)
# print("0" + str(res.tm_mday) if res.tm_mday < 10 else res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep="")
#
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%d/%m/%Y, %H:%M:%S"))

# start = time.monotonic()
# pause = 5
# print("Программа запущена...")
# time.sleep(pause)
# print("Пауза  была", pause, "секунд")
# finish = time.monotonic()
# res = finish - start
# print(res)

# Функции


# def hello(name, age):
#     print("Мне", age, ".Меня зовут", name)
#
#
# hello("Nikita",16)


# def get_sum(a, b):
#     print("Сумма: ", end="")
#     return a + b
#
#
# n = 2
# m = 5
# print(get_sum(n, m))
# res = get_sum(n, m)
# print(res ** 2)


# def maximum(one,two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9,6))
# print(maximum(9, 16))


# n = int(input("a = "))
# m = int(input("b = "))
#
#
# def qwerty(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# print("Результат: ", qwerty(n, m))


# def cub(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i,"в кубе = ",cub(i))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))


# def maximum(one,two):
#     if one > two:
#         return True
#     else:
#         return False
#
#
# print(maximum(9,6))
# print(maximum(9, 16))
#
# if maximum(9, 6):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")


# def check_password(password):
#     has_lower = False
#     has_upper = False
#     has_num = False
#     for ch in password:
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "0" <= ch <= "9":
#             has_num = True
#     if len(password) >= 8 and has_lower:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надёжный пароль")
# else:
#     print("Это ненадёжный пароль")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))


# def set_param(c=20, s="-"):
#     print(s * c, end="")
#     print()
#
#
# set_param()
# set_param(7)
# set_param(s="#")
# set_param(15, "+")


# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
#
# print("Сумма нечетных цифр: ")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge", age)
#
#
# display_info("Irina", 23)
# display_info(age=23, name="Irina")


# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)


# lt1 = [1, 20, 3]
# print(lt1, id(lt1[0]), id(lt1[1]))
# lt1[1] = 50
# print(lt1, id(lt1), id(lt1[0]), id(lt1[1]))

# Неизменяемые типы данных: int, str, float, bool, tuple
# Изменяемые типы данных: list

# Кортеж (tuple) - неизменяемый список

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# print(tpl[2])
# print(type(tpl))

# a = 1, 5, 9, 7, 8
# print(a, type(a))

# b = tuple()
# print(b, type(b))

# b = tuple("Hello")
# c = tuple(["Hello", "World"])
# print(b, c)

# a = (2, 9, 7, 3, 4)
# print(a[1:3])
# print(a[-1])

# tpl = tuple([i for i in range(5)])
# tpl = tuple(input("-> ") for i in range(5))
# print(tpl)

# tpl = tuple(2 ** i for i in range(1,13))
# print(tpl)

# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# # print(t3 * 2)
#
# print(t3.count("l"))
# print(t3.index('l'))


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             return tpl[first:(tpl.index(el, first+1)+1)]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# t = (10, 11, [1, 2, 3], [4, 5, 6], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "hi"
# t[4].append("new")
# print(t, id(t))


# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # firs_name, year, married = user
# firs_name, year, married = get_user()
# # print(user)
# print(firs_name, year, married)

# name = "Igor"
# if name:
#     print("Name:", name)
#     name = "Marina"
# else:
#     print("ELSE")
#
# print(name)

# name = "Igor"
#
# for i in range(5):
#     print(i, end=" ")
#     name = "Marina"
#
# print()
# print(name)

# name = "Igor"


# def func():
#     print("Hello")
#     name = "Marina"
#
# func()
# print(name)

# lst = [1, 2, 3, 4, 5]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst2 = list(tpl)
# print(lst2)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     count_name, country_population, cities = country
#     print("\nСтрана: ", count_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")

# Множества (set) - неупорядоченная коллекция, которая хранит только уникальные значения (изменяемый тип данных)

# s = {"red", "green", "blue", "red", "green"}
# print(type(s))
# print(s)
# print(len(s))
#
# for i in s:
#     print(i)

# a = set("Hello")
# print(a, type(a))
# from random import *
# s = {randint(20,50) for x in range(3)}
# print(s)

# s = {"red", "green", "blue"}
# print("green" in s)
# print("green" not in s)

# lst = ['ab_1', "ac_2", 'bc_1', 'bc_2']
# # lt = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst]
# lt = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c']
# print(lt)

# s = {"red", "green", "blue"}
# print(s)
# s.add("black")  # добавление элемента
# print(s)
# s.remove("black")  # удаляет элемент по значению (keyError)
# print(s)
# color = "green"
# if color in s:
#     s.remove(color)  # KeyError
# print(s)
# s.discard("green") # удаляет элемент по значению, не выбрасывает исключение, если элемента не существует
# print(s)
# color = s.pop() # удаляет первый элемент
# print(s)
# print(color)
# s.clear() # очищает множество
# print(s)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # a |= b
# c = a & b
# a &= b
# print(c)
# print(a)

# n = 5
# m = 6
# v = n + m
# print(v)
# n += m
# print(n)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
# one_hobby = drawing ^ music
# print(one_hobby)
# both_hobbies = drawing & music
# print(both_hobbies)
# drawing = drawing - both_hobbies
# print(drawing)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)
# print(a >= b)

# a = [1, 3, 2, 8, 4, 6, 3, 8, 4, 9, 4, 8, 4, 3]
# print(a)
# s = set(a)
# print(s)
# a1 = list(s)
# print(a1)

# s = frozenset("Hello")
# print(s)

# словари (dict)

# lst = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# lst[1] = 200
# d["two"] = 200
# print(lst)
# print(d)

# d = {"one": 1, "two": 2}
# print(d, type(d))
#
# d1 = dict(one=1, two=2)
# print(d1, type(d1))
#
# d2 = dict([["a", 1], ["b", 2]])
# print(d2, type(d2))

# d = {0: "text", "one": 45, (1, 2.3): "Кортеж", "список": [2, 3, 6, 7], True: 1,}
# print(d)
#
# key = 45
# if key in d:
#     del d[key]
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + str(key) + " нет в словаре")
# print(d)

# d["ne"] = "Новое значение"
# print(d)
#
# for key in d:
#     print(key, ":", d[key])

# print("one" in d)
# print("ne" in d)

# print(d[1, 2.3])


# a = {
#     "x1": 3,
#     "x2": 7,
#     "x3": 5,
#     "x4": -1
# }
# res = 1
# for key in a:
#     res *= a[key]
#
# print(res)


# d = dict()  # {}
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670', 3, 8500],
#     '3': ['Amd FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-43450', 5, 6400]
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Кол-во: "))
#                     goods[n][1] = count
#                     break
#                 except ValueError:
#                     print("Некорректно введено число")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")


# d = {'a': 1, 'b':2, 'c': 3}
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# for key, value in d.items():
#     print(key, "->", value)
# print(list[d.keys()])
# print(list(d.values()))
# print(list(d.items()))

# d = {'a': 1, 'b':2, 'c': 3}
# d2 = d
# print("D =", d)
# print("D2 =", d2)

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['b'])
# value = d.get('b', "такого ключа не существует")  # работает без выбрасывания ошибки
# print(value)
# item = d.setdefault("w")  # если ключа не существует, создаётся ключ со значением None
# print(item)
# print(d)
# item = d.pop('b', "Такого ключа не существует")
# print(item)
# print(d)
# item2 = d.popitem()  # удаляет последний элемент и возвращает кортеж удалённых значений
# print(item2)
# print(d)
# d.clear()
# print(d)

# d = dict.fromkeys(["a", "b"])
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'r': 7, 'q': 9}
# # d.update(d2)
# d3 = d.copy()
# d3.update(d2)
# d3 = d | d2
# print(d3)

# d = {"name": 'Kelly', 'age': 25, "salary": 8000, "city": "New York"}
# # new_d = dict()
# # new_d["name"] = d.pop("name")
# # new_d["salary"] = d.pop("salary")
# # print(d)
# # print(new_d)
# d["location"] = d.pop("city")
# print(d)

# d = {'один': 1, 'два': 2, "три": 3, "четыре": 4}
# new_d = {value: key for key, value in d.items() if value <= 2}
# print(new_d)

# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
# }
# # print(sales)
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ":", sales[x][y])
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])

# zip
# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# # c = (2.9, 3.7, 9.2)
# # d = dict(zip(a, b))
# d = list(zip(b, a))
# print(d)
# one = {'name': "Igor", "surname": "Doe", "job": "Consultant"}
# two = {'name': "Irina", "surname": "Smith", "job": "Manager"}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, "->", v2)

# lt = [(12, 'Dec'), (1, 'Jan'), (2, 'Feb')]
# a, b = zip(*lt)
# print(a)
# print(b)

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)
# print(len(b))

# first = {"one": 1, "two": 2}
# second = {"three": 3, "four": 4}
# print({**first, **second})
# for k, v in {**first, **second}.items():
#     print(k, "=>", v)

# colors = ['red', 'green', 'blue']
# i = 1
# for color in colors:
#     print(i, ") ", color, sep="")
#     i += 1
#
# for num, val in enumerate(colors, start=1):
#     print(num, ") ", val, sep="")

# studs = {}
# n = int(input("Кол-во студентов: "))
# # s = 0
# for i in range(n):
#     name = input(str(i + 1) + "-й студент: ")
#     point = int(input("Балл: "))
#     studs[name] = point
#     # s += point
#
# s = sum(studs.values())
# avg = s / n
# print(studs)
# print(s)
# print("Средний балл:", avg)
# for i in studs:
#     if studs[i] > avg:
#         print(i)

# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 6, 8, "abc"))


# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3))
# print(summa(1, 2, 3, 4))


# def ch(*args):
#     avg = sum(args) / len(args)
#     print(avg)
#     res = []
#     for num in args:
#         if num < avg:
#             res.append(num)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(5))


# def print_scores(student, *scores):
#     print("Stident name: ", student, end=", Оценки: ")
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_scores("Jonathan", 100, 95, 88, 92, 99, 84)
# print_scores("Rick", 96, 20, 33, 66)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(one="один"))

# def intro(**data):
#     for k, v in data.items():
#         print(k, "is", v)
#
#
# intro(name="Irina", surname="Sharma", age=22)
# intro(name="Igor", surname="Wood", email="igor@mail.ru",country="Russia", age=22, phone=9876543210)


# def func(a, b, *args):
#     return a, b, args
#
#
# print(func(5, 1, 2, 3, 4, 5, 6, 7))


# my_dict = {"one": 'first'}
#
#
# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# print(my_dict, my_dict)
# db(k1=22, k2=31, k3=11, k4=91)
# print(my_dict, my_dict)
# db(name='Bob', age=31, weight=61, eyes_color='grey')

# name = "Tom"  # глобальная переменная
#
#
# def hi():
#     global name, surname
#     name = "Sam"
#     surname = "Johnson"  # локальная переменная
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()
# print(name)
# print(surname)


# def add(a):
#     x = 2
#
#     def outer():
#         # x = 3
#         print("x =", x)
#         return a + x
#     return outer()
#
#
# print(add(5))


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#
#     inner()
#     print('a =', a)
#     t = a
#
#
# fn()
# c = x + t
# print(c)


# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#         fn3()
#         print("fn2.x", x)
#     fn2()
#     print("fn1.x", x)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))


# Замыкание - функция возвращает другую функцию, но не вызывает её

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# item1 = outer(5)
# print(item1(10))
#
# item2 = outer(6)
# print(item2(10))

# print(outer(7)(10))


# def func(a):
#     return a * 2
#
#
# x = func(5)
# print(x)

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         b = b + "_new"
#         a += 1
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
# res2()


# lambda - выражения

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)(10, 20))
#
#
# def func(x, y):
#     return x + y
#
#
# # func = lambda x, y: x + y
# print(func(1, 2))


# print((lambda a, b, c: a + b + c)(10, 20, 30))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4
# )
# for t in c:
#     print(t("abc_"))


# def inc1(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# func = inc1(10)
# print(func(5))
#
# def inc2(n):
#     return lambda x: n + x
#
#
# func2 = inc2(10)
# print(func2(5))
#
# inc3 = (lambda n: (lambda x: n + x))
#
# func3 = inc3(10)
# print(func3(5))
#
# print((lambda n: (lambda x: n + x))(10)(5))


# d = {'a': 15, 'c': 10, 'b': 5}
# # lst = sorted(d.items())
# lst = list(d.items())
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))


# players = [
#     {"name": "Антон", "last_name": "Бирюков", "rating": 9},
#     {"name": "Алексей", "last_name": "Бодня", "rating": 10},
#     {"name": "Федор", "last_name": "Сидоров", "rating": 4},
#     {"name": "Михаил", "last_name": "Семенов", "rating": 6},
# ]
#
# res = sorted(players, key=lambda item: item["last_name"])
# print(res)
#
# res1 = sorted(players, key=lambda item: item["rating"], reverse=True)
# print(res1)


# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(a[1](8, 3))
# print(a[2](8, 3))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье")
# }
#
# d[6]()
# from math import pi
# area = {
#     "Circle": lambda radius: pi * radius * radius,
#     "Rectangle": lambda a, b: a * b,
#     "Trapezoid": lambda a, b, h: (a + b) * h / 2
# }
#
# print("Площадь окружности:", area["Circle"](2))
# print("Площадь прямоугольника:", area["Rectangle"](10, 13))
# print("Площадь трапеции:", area["Trapezoid"](7, 5, 3))


# print((lambda a, b: a if a > b else b)(5, 10))

# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))

print("Вносим изменения")


