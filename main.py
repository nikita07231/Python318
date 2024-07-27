# name = "Nikolay"
# print("Hello,", name, "!")
# import curses.ascii
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

# print("Вносим изменения")
# print("Данные переносим на GitHub")


# map(func, iterable), filter(func, iterable)

# def mult(t):
#     return t * 2


# lst = [2, 8, 12, -5, -10]
#
# # lst2 = list(map(mult, lst))
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)


# t = (2.88, -1.75, 100.55)
#
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = dict(map(lambda x, y: (x, y), st, num))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)


# t = ('abcd', 'abc', 'asdfg', 'def', 'ert')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)


# b = [60, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# from random import *
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# lst2 = list(filter(lambda x: 10 <= x <= 20, lst))
# print(lst2)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)

# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())


# def my_decorator(func):
#     def inner():
#         print("Code before")
#         func()
#         print("Code after")
#     return inner
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def inner():
#         print("*" * 40)
#         func()
#         print("*" * 40)
#     return inner
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# func_test()


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции: ", count)
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(name, surname):
#     print("Меня зовут", name, surname)
#
#
# print_full_name("Ирина", "Ветрова")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "Изучают", study, "\n")
#
#
# print_full_name("Ирина", "Борис", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(arg):
#     def decor(fn):
#         def wrap(*args, **kwargs):
#             return arg * fn(*args, **kwargs)
#
#         return wrap
#     return decor
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


# Строки
# print(0o10)
# print(bin(18))
# print(oct(18))
# print(hex(18))
#
# print(0b10010)


# q = "Pyt"
# w = 'hon'
# e = q + w
# print(e)
# # print(e * 3)
# # print("y" in e)
# # print(e[1])
# # print(e[-1])
# e = e[:3] + 't' + e[4:]
# print(e)

# print("Привет")
# print(u"Привет")

# print("C:\\folder\\file.txt")
# print(r"C:\folder\\"[:-1])

# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет")

# print(f"Число {round(12.2564, 2)}")
# print(f"Число: {12.2564:.2f}")

# s = """Строка символов"""
# print(s)

# def square(n):
#     """Принимает число n, возвращает 2n"""
#     return n ** 2
#
#
# print(square(5))

# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#     :param r:
#     :param h:
#     :return:
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord("a"))
# print(ord("й"))

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# st = "Test string for ne"
# arr = [ord(x) for x in st]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое", arr)
# arr += [ord(x) for x in input("->")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)

# print(chr(97))

# a = 122
# b = 97
# # if a > b:
# #     for i in range(b, a + 1):
# #         print(chr(i), end=" ")
# # else:
# #     for i in range(a, b + 1):
# #         print(chr(i), end=" ")
# if b > a:
#     a, b = b, a
# for i in range(b,a + 1):
#     print(chr(i), end=" ")


# print("apple" == "Apple")

# from random import randint
#
# min_ascii = 33
# max_ascii = 126
# shortest = 6
# longest = 16
#
#
# def random_password():
#     res = ""
#     for i in range(randint(shortest, longest)):
#         res += chr(randint(min_ascii, max_ascii))
#     return res
#
#
# print("Ваш случайный пароль:", random_password())

# Методы слов

# s = "hello, World! I am learning Python."
# # a = s.capitalize()
# # print(a)
# # print(s.lower())
# # print(s.upper())
# print(s.count("h"))

# print(s.find("Python"))
# print(s.index("Python"))

# print(s.find("h", 1, -4))
# print(s.rfind("h"))
# print(s.rindex("h"))

# st = input("Введите два слова через пробел: ")
# first = st[: st.find(" ")]
# second = st[st.find(" ") + 1:]
# print(second, first)

# print(s.endswith("on."))
# print(s.startswith("I am", 14))
# print(s.find("I am"))

# a = input("Введите число: ")
# try:
#     a = int(a)
#     print(a ** 2)
# except ValueError:
#     print("Нужно ввести число")

# print('123'.isdigit())

# a = input("Введите число: ")
# b = 2
# if a.isdigit():
#     a = int(a)
#     print(a + b)
# else:
#     print(a + str(b))


# print("abc123".isalnum())  # состоит ли строка только из букв и цифр
# print("ABCabc".isalpha())  # состоит ли строка только из букв


# print("abc".islower())  # определяет, являются ли буквенные символы строки в нижнем регистре
# print("ABC123.".isupper())  # определяет, являются ли буквенные символы строки в верхнем регистре

# print('py'.center(10))
# print('py'.center(10, "-"))

# print("     py     ".lstrip())
# print("     py     ".rstrip())
# print("     py     ".strip())
#
# print("https://www.python.orgw".lstrip("/:pthsw"))
# print("https://www.python.orgw".strip("/:pthsw"))

# s = "hello, Python! I am learning Python. Python"
# print(s.replace("Python", "Java", 2))

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(["1", "2"]))  # объединяет итерируемый объект в строку через символ разделитель
#
# print(":".join("Hello"))

# print("a b c".split())
# print("www.python.org".split(".", 1))
# print("www.python.org".rsplit(".", 1))

# Регулярные выражения

# import re

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
#
# reg = r"[204]"
# # print(re.findall(reg, s))  # возвращает список найденных совпадений
# # print(re.search(reg, s))  # возвращает первое совпадение с шаблоном
# print(re.findall(reg, s))

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# pattern = "[0-2][0-3]:[0-5][0-9]"
# print(re.findall(pattern, st))

# s = r"Я ищу совпадения в 2024 году. И я их найду в 2 счё_та."
# # reg = r"\d"  # [0-9]
# # reg = r"\D"  # [^0-9]
# # reg = r"\s  # [ ]
# # reg = r"\S"  # [^ ]
# # reg = r"\w"  # [0-9A-zА-я_]
# # reg = r"\W"  # [^0-9A-zА-я_]
# print(re.findall(reg, s))

# кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1 повторений

# st = "05-06-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"\s#.*", "", st))

# st = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 18"
# pattern = r"\w+\s*=\s*[\w\s.]+"
# print(re.findall(pattern, st))

# s1 = "12 сентября 2024 года"
# reg1 = r"\d{2,4}"
# print(re.findall(reg1, s1))

# s = r"Я ищу совпадения в 2024 году. И я их найду в 2 счё_та."
# reg = r"\w+\s\w+\.$"
# print(re.findall(reg, s))


# def valid_login(name):
#     return re.findall("^[A-Za-z0-9_-]{3,16}$", name)
#
#
# print(valid_login("Python_master"))
# print(valid_login("Pyt#@!hon"))

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# text = "Hello World"
# print(re.findall(r"\w+", text, re.DEBUG))

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счё_та."
# reg = "я"
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one # Комментарий
# two
# """
#
# # print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one.\w+", text, re.DOTALL))
#
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+ # part 1
# @
# [a-z.-]+
# """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?mi)^python"
# print(re.findall(reg, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))
#
# s1 = "12 сентября 2024 года 4567897"
# reg1 = r"\d{2,4}?"
# print(re.findall(reg1, s1))

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = r'Ольга|Виталий'
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0"
# reg = r"(int|float)\s*=\s*[.\w+]*"
# print(re.findall(reg, s))

# (?:...) - обозначает, что эта группирующая скобка является не сохраняющей

# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))


# a = "28-08-2021"
# pattern = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19\d\d|20[0-9][0-9])"
# print(re.findall(pattern, a))
# print(re.search(pattern, a))
# m = re.search(pattern, a)
# print(m[0])
# print(m[1])
# s = "Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024"
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))

# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На коком вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(354, 10))

# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# names = ["Adam", ["Bob", ["Chat", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# # print(isinstance(names, list))
# # print(isinstance(names[0], list))
# print(count_items(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\n" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" Hello\nWord"))


# f = open("test.txt")
# print(f)
# print(*f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# f.close()

# f = open("test.txt", "r")
# print(f.read(3))
# print(f.read())
# f.close()

# f = open("test1.txt")
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open("test1.txt")
# print(f.readlines(16))
# print(f.readlines())
# f.close()

# f = open("test1.txt")
# count = 0
# for line in f:
#     count += 1
# print(count)
# f.close()

# f = open("test1.txt")
# print(len(f.readlines()))
# f.close()

# f = open("xyz.txt", "w")
# f.write("Hello\nWorld!")
# f.close()

# f = open("xyz1.txt", "a")
# f.write("\nNew text")
# f.close()


# f = open("xyz.txt", "w")
# f.writelines(['This is line 1\n', 'This is line 2\n'])
# f.close()

# lst = [i for i in range(1, 20)]
# print(lst)
#
# f = open("xyz.txt", "w")
# for index in lst:
#     f.write(str(index))
# f.close()
#
# f = open("xyz.txt")
# d = f.read()
# print(d)
# print(type(d))
# f.close()

# lst = [i for i in range(1, 20)]
# print(lst)
#
# f = open("xyz.txt", "w")
# f.write("\t".join(map(str, lst)))
# f.close()
#
# f = open("xyz.txt")
# d = f.read()
# st = list(map(int, d.split("\t")))
# print(st)
# print(type(st))
# f.close()

# file = "text2.txt"
#
# f = open(file, "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open(file)
# read_line = f.readlines()
# print(read_line)
# read_line[1] = "Hello world!\n"
# print(read_line)
# f.close()
#
# f = open(file, "w")
# f.writelines(read_line)
# f.close()

# file = "text2.txt"
#
# f = open(file, "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open(file)
# s = f.readlines()
# f.close()
# print(s)
#
# pos = int(input("pos = "))
# if 0 <= pos < len(s):
#     del s[pos]
# else:
#     print("Индекс введен неверно")
# print(s)
#
# f = open(file, "w")
# f.writelines(s)
# f.close()

# f = open("test.txt")
# print(f.read(3))
# print(f.tell())  # позиция условного курсора
# print(f.seek(1))  # перемещение условного курсора в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open("test.txt", "r+")
# f.write("I am learning Python")
# print(f.seek(3))
# f.write("-new string-")
# f.close()

# f = open("test.txt", "r+")
# f.write("I am learning Python")
# print(f.seek(3))
# f.write("-new string-")
# print(f.read())
# f.close()

# with open("test.txt", "w") as f:
#     print(f.write("012\n34567\n89"))
# print(f.closed)

# with open("test.txt", "r") as f:
#     for line in f:
#         print(line)

# def longest_words(file):
#     with open(file, "r", encoding="utf-8") as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         print(max_length)
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words("test.txt"))

# one = "one.txt"
# two = "two.txt"
# three = "three.txt"

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open(one, "w") as f:
#     f.write(text)

# with open(one, "r") as fr, open(two, "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)

# one = "one.txt"
# two = "two.txt"
# three = "three.txt"
#
# # with open(one, "r") as f1:
# #     a = f1.readlines()
# #     print(a)
# #
# # with open(two, "r") as f2:
# #     b = f2.readlines()
# #     print(b)
# #
# # c = a + b
# # print(c)
# #
# # with open(three, "w") as f3:
# #     f3.writelines(c)
#
# with open(one, "r") as f1, open(two, "r") as f2, open(three, "w") as f3:
#     a = f1.readlines()
#     b = f2.readlines()
#     c = []
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     print(a)
#     print(b)
#     print(c)
#     f3.writelines(c)

# file = "text2.txt"
#
# f = open(file)
# line = 0
# for i in f:
#     line += 1
#     word = 0
#     flag = 0
#     for j in i:
#         if j != " " and flag == 0:
#             word += 1
#             flag = 1
#         elif j == " ":
#             flag = 0
#
#     print(i, len(i), "Символов", word, "слов")
#
# print(line, "Строки в документе")
# f.close()

# import os
# import os.path

# import main

# print(os.path.split(r""))


# print(os.getcwd())  # путь к рабочей директории
# print(os.listdir())  # список директорий и файлов
# print(os.listdir(".."))
#
# os.mkdir("folder1")  # создать папку
# os.makedirs("nested1/nested2/nested3")  # создаёт папку с промежуточными папками в пути
# os.remove("folder1/1.txt")  # удалить файл
# os.rmdir("folder1")  # удалить папку, но пустую

# os.rename("xyz1.txt", "test2.txt")
# os.rename("folder", "test")  # переименовывает файлы или папки

# os.rename("xyz.txt", "test/xy.txt")

# os.renames("two.txt", "text/t.txt")  # переименовывает файлы или папки и перемещает их по несуществующему пути путём его создания

# for root, dirs, files in os.walk("nested1", topdown=False):
#     print("Root:", root)
#     print("\tSubdirs:", dirs)
#     print("\tFiles:", files)


# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена")
#     print("-" * 50)
#
#
# remove_empty_dirs("nested1")

# dirs = [r'Work\F1',  r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', "f13.txt"],
#     r"Work\F2F21": ['f211.txt', 'f212.txt']
# }
# for d, f in files.items():
#     print(f)
#     for file in f:
#         file_path = os.path.join(d, file)
#         open(file_path, "w").close()
#
# files_with_text = [r"Work\w.txt", r'Work\F1\f12.txt', r"Work\F2F21\f211.txt", r'Work\F2F21\f212.txt']
#
# for file in files_with_text:
#     with open(file, "w") as f:
#         f.write(f"Текст для файла {file}")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root}")
#
#
# print_tree("Work", False)
# print_tree("Work", True)

# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# ['f211.txt', 'f212.txt']
# Work\F2F21\f211.txt
# Work\F2F21\f212.txt

# print(os.path.exists())  # возвращает True если существует в файловой системе
# import time
# path = "main.py"
# # print(os.path.getsize(path) / 1024)
#
# print(os.path.getctime(path))  # время создания файла
# print(os.path.getatime(path))  # время последнего доступа к файлу
# print(os.path.getmtime(path))  # время последнего изменения файла (в секундах)
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getctime(path))))

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)
# Point.set_coord(p1, 2, 4)
#
# p2 = Point()
# # p2.x = 3
# # p2.y = 7
# p2.set_coord(3, 7)

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональный данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # устанавливаем новое имя
#         self.name = name
#
#     def get_name(self):  # получаем имя
#         return self.name
#
#     def set_birthday(self, value):
#         self.birthday = value
#
#     def get_birthday(self):
#         return self.birthday
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Юлия")
# print(h1.get_name())
# h1.set_birthday("25.05.1986")
# print(h1.get_birthday())


# class Person:
#     skill = 10  # статическое свойство
#
#     def __init__(self, name, surname):  # Инициализатор
#         self.name = name  # динамические свойства
#         self.surname = surname
#         print("Инициализатор класса Person")
#
#     def __del__(self):
#         print("Удаление экземпляра класса")
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, end="\n\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
#
# # del p1
# p1 = 5
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def get_coord(self):
#         print(self.__dict__)
#
#
# p1 = Point(5, 10)
# p1.get_coord()
# print(p1.count)
#
# p2 = Point(3, 7)
# p2.get_coord()
# print(p2.count)
#
# p3 = Point(8, 16)
# p3.get_coord()
#
# print(Point.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def say_hi(self):
#         print(f"Приветствую! Меня зовут:", self.name)
#
#     def __del__(self):
#         print(self.name, "выключается")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "Был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
#
# del droid1
# del droid2
#
# print("Численность роботов:", Robot.k)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def __check_value(s):
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# p1.set_coord(100, 500)
# print(p1.get_coord())
# # print(p1.__x, p1.__y)
# # p1.__x = 100
# # p1.__y = "abc"
# # # print(p1.x, p1.y)
# print(p1.__dict__)
# import math
#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(s):
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def set_width(self, value):
#         if Rectangle.__check_value(value):
#             self.__width = value
#
#     def set_length(self, value):
#         if Rectangle.__check_value(value):
#             self.__length = value
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def get_area(self):
#         return self.__length * self.__width
#
#     def get_perimeter(self):
#         return 2 * (self.__length + self.__width)
#
#     def get_hypotenuse(self):
#         return round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)
#
#     def draw(self):
#         print(("*" * self.__width + "\n") * self.__length)
#
#
# a = Rectangle(4, 12)
# a.set_length(3)
# a.set_width(9)
# print("Длина прямоугольника:", a.get_length())
# print("Ширина прямоугольника:", a.get_width())
# print("Площадь прямоугольника:", a.get_area())
# print("Периметр прямоугольника:", a.get_perimeter())
# print("Гипотенуза прямоугольника:", a.get_hypotenuse())
# a.draw()


# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y, z):
#         self.__x = x
#         self.__y = y
#         self.z = z
#
#
# p1 = Point(5, 10, 15)
# # p1.z = 15
# # print(p1.__dict__)
# print(p1.z)


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         self.__x = x
#         print("__set_x")
#
#     def __get_x(self):
#         print("__get_x")
#         return self.__x
#
#     x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# # p1.x = 9
# print(p1.x)
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должны быть числом")
#
#     def __check_value(s):
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     # x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# p1.x = 9
# # print(p1.x)
# print(p1.__dict__)


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 'h'


# class Point:
#     __count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point(5, 10)
# p2 = Point(5, 10)
# p3 = Point(5, 10)
#
# print(Point.get_count())
# print(p1.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         mx = a
#         if b > mx:
#             mx = b
#         if c > mx:
#             mx = c
#         if d > mx:
#             mx = d
#         return mx
#
#     @staticmethod
#     def min(*args):
#         mn = args[0]
#         for i in args:
#             if i < mn:
#                 mn = i
#         return mn
#
#     @staticmethod
#     def average(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def factorial(n):
#         mul = 1
#         for i in range(1, n + 1):
#             mul *= i
#         return mul
#
#
# print("Максимальное число:", Numbers.max(3, 5, 7, 9))
# print("Минимальное число:", Numbers.min(3, 5, 7, 9))
# print("Среднее арифметическое:", Numbers.average(3, 5, 7, 9))
# print("Факториал числа:", Numbers.factorial(5))


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         date = Date(day, month, year)
#         return date
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#
# dates = [
#     "23.10.2024",
#     "21/12/2023",
#     "01.01.2022",
#     "12.31.2021"
# ]
#
# for i in dates:
#     if Date.is_date_valid(i):
#         date = Date.from_string(i)
#         print(date.string_to_db())
#     else:
#         print(f"Неправильная дата или  формат строки с датой")
# date1 = Date.from_string("23.10.2024")
# print(date1.string_to_db())
# date2 = Date.from_string("21.12.2013")
# print(date2.string_to_db())
# string_date = "23.10.2024"
# print(date.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет №{self.num} принадлежащий {self.surname} был открыт")
#         print("*" * 50)
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_weight(weight)
#         self.__fio = fio
#         self.__old = old
#         self.__password = ps
#         self.__weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall("[a-zа-яё-]", fio, re.IGNORECASE))
#         # print(letters)
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float):
#             raise TypeError("Вес должен быть вещественным числом")
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)


# Наследование

# class Point(object):
#     def __init__(self, x, y):
#         self.__x = x
#         self.y__ = y
#
#
# print(issubclass(Point, object))

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#
#     def draw_line(self) -> None:
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color} {self._width}")
#
#
# class Rect:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw_rect(self) -> None:
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color} {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         self.__width = width
#         self.__height = height
#         super().__init__(color)
#
#     def area(self):
#         print(f"Прямоугольник {self.color}. Площадь: ", end="")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# print(rect.area())


# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = "Smith"
#             self.id = "657"
#
#         def show(self):
#             print("Name:", self.name)
#             print("Id:", self.id)
#             print("*" * 20)
#
#     class Head:
#         def __init__(self):
#             self.name = "Boss"
#             self.id = "789"
#
#         def show(self):
#             print("Name:", self.name)
#             print("Id:", self.id)
#             print("*" * 20)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
#
# d1.show()
# d2.show()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = [Cat("Пушок")]
# print(cat)


# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(5, 7)
# print(len(p))
# p1 = Point(4, 6, 8)
# print(len(p1))


# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(10, 20)
# print(p1.x, p1.y)
# p1.z = 30
# print(p1.z)


# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(10, 20)
# p2 = Point2D(10, 20)
# print("pt1 =", p1.__sizeof__())
# print("pt2 =", p2.__sizeof__())


# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     pass
#
#
# pt = Point(1, 2)
# pt3 = Point(10, 20)


# Множественное наследование


# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is slipping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# dog = Dog("Buddy")
# dog.bark()
# dog.sleep()
# dog.play()


# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(A):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализатор класса D")
#
#
# d = D()


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point):
#         self._sp = sp
#         self._ep = ep
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line()


# Миксины

# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         MixinLog.ID += 1
#         self.id = self.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
#
# n = Notebook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()


# Перегрузка оператора

# class Clock:
#     __Day = 86400  # число секунд в дне
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__Day
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)

#
# c1 = Clock(100)
# print(c1.get_format_time())
# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy"
#         elif self.pol == "F":
#             return f"{self.name} is good girl"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         return [Cat("No name", 0, choice(["M", "F"])) for _ in range(randint(1, 5))]
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Else", 5, "F")
# cat3 = Cat("Murzik", 3, "M")
# print(cat1)
# print(cat2)
# print(cat1 + cat2)


# class Student:
#     def __init__(self, name, *args):
#         self.name = name
#         self.marks = args
#
#
# s1 = Student("Сергей", 5, 5, 3, 4, 5)
# print(s1.marks[2])


# class Clock:
#     __Day = 86400  # число секунд в дне
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__Day
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         if item == "min":
#             return self.sec // 60 % 60
#         if item == "sec":
#             return self.sec % 60
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
#
# print(c1["hour"], c1["min"], c1["sec"])


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimeter(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimeter(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimeter(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimeter())


# Функторы

# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()


# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = string_strip("?:!.; ")
# print(s1(" Hello World! "))
# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Init ActualClass()")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))


# Дескриптор
# __get__()
# __set__()
# __delete__()
# __set_name__()

# class String:
#     def __init__(self, value):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{value} должно быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     if not isinstance(value, str):
#     #         raise TypeError(f"{value} должно быть строкой")
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     if not isinstance(value, str):
#     #         raise TypeError(f"{value} должно быть строкой")
#     #     self.__surname = value
#
#
# p = Person(12, "Petrov")

# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value

#
# class Person:
#     first_name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, first_name, surname):
#         self.first_name = first_name
#         self.surname = surname
#
#
# p = Person(12, "Petrov")
# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise ValueError(f"{coord} должно быть целым числом")
#
#     def __set_name__(self, owner, name):
#         self.__name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         instance.__dict__[self.__name] = value
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)


# Метаклассы

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)
# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# lst.append(9)
# print(lst, lst.get_length())


# Создание модулей
# import rect
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimeter(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimeter(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimeter(self):
#         return self.a + self.b + self.c


# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
#
# s1 = rect.Square(10)
# s2 = rect.Square(20)
#
# t1 = rect.Triangle(1, 2, 3)
# t2 = rect.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimeter())
# from car import electrocar
#
#
# e_car = electrocar.ElectroCar("Tesla", "T", 2018, 99000)
# e_car.show_car()
# e_car.description_battery()


# Упаковка данных (сериализация)
# Распаковка данных (десериализация)

# marshal
# pickle
# json
# import pickle
#
# file_name = "basket.txt"
#
# shop_list = {
#     "фрукты": ["яблоки", "груши"],
#     "овощи": ("морковь",),
#     "бюджет": 1000
# }
#
# with open(file_name, "wb") as f:
#     pickle.dump(shop_list, f)
#
# with open(file_name, "rb") as f:
#     shop_list_2 = pickle.load(f)
#
# print(shop_list_2)


# class Test:
#     num = 35
#     string = "Привет"
#     lst = [1, 2, 3]
#     tpl = (25, 98)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.string}\nСписок: {Test.lst}\nКортеж: {Test.tpl}"
#
#
# obj = Test()
# # print(obj)
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
#
# new_obj = pickle.loads(my_obj)
# print(new_obj)


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# # print(item1)
#
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
# print(item3)


# import json
#
# data = {
#     'name': 'Olga',
#     'age': 20,
#     20: None,
#     1: True,
#     False: 0,
#     'hobbies': ('running', 'string'),
#     'children': {
#         'first_name': ['Alice', 'Bob'],
#         'age': [6, 12]
#     }
# }
#
# with open("data_file.json", "w") as f:
#     json.dump(data, f, indent=4)
# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         st = ""
#         for i in self.marks:
#             st += str(i) + ", "
#         return f"{self.name}: {st[:-2]}"
#
#     def add_mark(self, new_mark):
#         self.marks.append(new_mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return sum(self.marks) / len(self.marks)
#
#     def dum_to_json(self, file_name):
#         data = {"name": self.name, "marks": self.marks}
#         with open(file_name, "w") as f:
#             json.dump(data, f)
#
#     def load_from_file(self, file_name):
#         with open(file_name, "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         st = ""
#         for i in self.students:
#             st += str(i) + "\n"
#         return f"Group: {self.group}\n{st}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         self.students.pop(index)
#
#     def dump_group(self, file_name):
#         with open(file_name, "w") as f:
#             stud_list = []
#             for i in self.students:
#                 stud_list.append([i.name, i.marks])
#             json.dump(stud_list, f, indent=2)
#
#     @staticmethod
#     def change_group(gr1, gr2, index):
#         return gr2.add_student(gr1.remove_student(index))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(2)
# # print(st1)
# # st1.edit_mark(4, 5)
# # print(st1)
# # print(st1.average_mark())
# file = "student.json"
# st1.dum_to_json(file)
# st1.load_from_file(file)
# st2 = Student("Nikolaenko", [2, 3, 5, 4, 4, 2])
# st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
# sts1 = [st1, st2]
# group1 = Group(sts1, "GK Python")
# group1.add_student(st3)
# # print(group1)
# # print()
# group1.remove_student(1)
# # print(group1)
# sts2 = [st2]
# group2 = Group(sts2, "GK Web")
# # print(group2)
# # print("." * 20)
# Group.change_group(group1, group2, 0)
# # print(group1)
# # print()
# # print(group2)
# import json
#
# data = {}
#
#
# class CountryCapital:
#     def __init__(self, country, capital):
#         self.country = country
#         self.capital = capital
#         data[self.country] = self.capital
#
#     def __str__(self):
#         return f"{self.country}: {self.capital}"
#
#     @staticmethod
#     def add_country(filename):
#         country_name = input("Введите страну: ")
#         capital_name = input("Введите название столицы: ")
#
#         try:
#             date = json.load(open(filename))
#         except FileNotFoundError:
#             date = {}
#
#         date[country_name] = capital_name
#
#         with open(filename, "w") as f:
#             json.dump(date, f, indent=2)
#
#     @staticmethod
#     def load_from_file(filename):
#         with open(filename, "r") as f:
#             print(json.load(f))
#
#
# file = 'list_capital.json'
# index = ''
# while index != "6":
#     index = input("Действие:\n1 - добавление данных\n2 - удаление данных\n6 - завершение работы\nВвод: ")
#     if index == "1":
#         CountryCapital.add_country(file)
#     if index == "5":
#         CountryCapital.load_from_file(file)


# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # print(response.text)
# # print(type(response.text))
# todos = json.loads(response.text)
# # print(todos)
# # print(type(todos[0]))
#
# todos_by_user = {}
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
#
# print(todos_by_user)
#
# top_user = sorted(todos_by_user.items(), key=lambda x:x[1], reverse=True)
# print(top_user)
#
# max_complete = top_user[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_user:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
# # users = ["5"]
# max_users = " and ".join(users)
# s = "s" if len(users) > 1 else ""
# print(f"user{s} {max_users} completed {max_complete} TODOs")
#
#
# def keep(tod):
#     is_completed = tod['completed']
#     has_max_count = str(tod["userId"]) in users
#     return is_completed and has_max_count
#
#
# with open("filtered_data.json", "w") as f:
#     filtered = list(filter(keep, todos))
#
#     json.dump(filtered, f, indent=2)


# import csv

# with open("data.csv") as f:
#     file_reader = csv.reader(f, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]}")
#         count += 1


# with open("data.csv") as f:
#     field_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=field_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"\t{row['Имя']} - {row['Профессия']}. Год рождения {row['Год рождения']}")
#         count += 1


# with open("student.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", 5, 12])
#     writer.writerow(["Маша", 11, 18])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]

# with open("data_new.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)

# with open("student1.csv", "w") as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": 6})
#     writer.writerow({"Имя": "Маша", "Возраст": 15})
#     writer.writerow({"Имя": "Вова", "Возраст": 14})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]

# with open("dict_writer.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)


# from bs4 import BeautifulSoup
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find('div', class_='row')
# row = soup.find_all('div', class_='row')[1].find('div', class_='name').text
# row = soup.find_all('div', {"data-set": "salary"})[0].text
# row = soup.find('div', string="Alena").parent
# row = soup.find('div', string="Alena").find_parent(class_="row")
# row = soup.find('div', id="whois3").find_next_sibling()
# row = soup.find('div', id="whois3").find_previous_sibling()
# print(row)


# from bs4 import BeautifulSoup


# def get_copywriter(tag):
#     whois = tag.find('div', class_="whois").text
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
#
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
#
# print(copywriter)


# from bs4 import BeautifulSoup
# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
# salary = soup.find_all("div", {"data-set": "salary"})
# for i in salary:
#     get_salary(i.text)


# import requests
#
#
# r = requests.get("https://ru.wordpress.org/")
# # print(r)
# # print(r.status_code)
# # print(r.headers)
# # print(r.content)
# print(r.text)


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[1]
#     plugins = p1.find_all("div", class_="entry")
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         url = plugin.find("h3").find("a").get("href")
#         rating = plugin.find("span", class_="rating-count").text
#         r = refined(rating)
#         data = {'name': name, "url": url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open("plugins1.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data['name'], data["url"], data['active'], data["cy"]))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     elements = soup.find_all("div", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find("h3", class_="entry-title").text
#         except AttributeError:
#             name = ""
#
#         try:
#             url = el.find("h3", class_="entry-title").find('a')["href"]
#         except AttributeError:
#             url = ""
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except AttributeError:
#             active = ""
#
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except AttributeError:
#             cy = ""
#
#         data = {
#             'name': name,
#             'url': url,
#             'active': active,
#             'cy': cy
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(2, 3):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# from parsers import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()


# import sqlite3


# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
#
# cur.execute("""
# """)
#
# con.close()


# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     data BLOB)""")
#
#     cur.execute("DROP TABLE users")
#
#
# import sqlite3
#
#
# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS person(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB NOT NULL DEFAULT "+79090000000",
#     age INTEGER CHECK(age > 0 AND age < 100),
#     email TEXT UNIQUE
#     )""")
#
#     переименовать таблицу
#     cur.execute("""
#     ALTER TABLE person
#     RENAME TO person_table;
#     """)
#
#     добавить поле в таблицу
#     cur.execute("""
#         ALTER TABLE person_table
#         ADD COLUMN address
#         """)
#
#     удалить столбец
#     cur.execute("""
#         ALTER TABLE person_table
#         DROP COLUMN address
#         """)


# import sqlite3
#
#
# with sqlite3.connect("db_3.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""
#     SELECT *
#     FROM T1
#     LIMIT 2, 5
#     """)
#
#     for i in cur:
#         print(i)
#
#     res = cur.fetchone()
#     print(res)
#
#     res2 = cur.fetchmany(2)
#     print(res2)
#
#     res3 = cur.fetchall()
#     print(res3)

#
# import sqlite3
#
# cars_list = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 36000),
#     ('Citroen', 29000),
#     ('Honda', 33000)
# ]
#
# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
#     # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars_list)
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)
#
#     for car in cars_list:
#         cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)
#
#     cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
#     cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
#     cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
#     cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
#     cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")


# import sqlite3
#
# con = None
# try:
#     con = sqlite3.connect("car.db")
#     cur = con.cursor()
#     cur.executescript("""
#         CREATE TABLE IF NOT EXISTS cars(
#             car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             model TEXT,
#             price INTEGER
#         );
#         BEGIN;
#         INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#         UPDATE cars SET price = price + 100;
#         """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()


# import sqlite3
#
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)
#
#     # cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     # last_row_id = cur.lastrowid
#     # buy_car_id = 2
#     # cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))
#
#     cur.execute("SELECT model, price FROM cars")
#
#     rows = cur.fetchone()
#     print(rows)
#
#     rows1 = cur.fetchmany(5)
#     print(rows1)
#
#     rows2 = cur.fetchall()
#     print(rows2)
#
#     for res in cur:
#         print(res[0], "->", res[1])
#
# import sqlite3
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     )
#     """)
#
#     # img = read_ava(1)
#     # if img:
#     #     binary = sqlite3.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))
#
#     cur.execute("SELECT ava FROM users")
#     img = cur.fetchone()['ava']
#
#     write_ava("out.png", img)


# import sqlite3


# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "w") as f:
#         for sql in con.iterdump():
#             f.write(sql)


# with sqlite3.connect("car_project.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)


# import os
#
# from models.database import DATABASE_NAME, Session
# import create_database as db_creator
#
# from models.lesson import Lesson, association_table
# from models.student import Student
# from models.group import Group
#
#
# if __name__ == "__main__":
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()
#
#     session = Session()
#     print(session.query(Lesson).all())
#     print("*" * 60)


#  Шаблонизатор (Jinja)

# from jinja2 import Template

# # name = "Игорь"
# # age = 25
# per = {'name': 'Игорь',
#        'age': 25}
#
# tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.name }}.")
#
# msg = tm.render(p=per)
# # msg = tm.render(n=name, a=age)
# print(msg)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#
# per = Person("Игорь", 25)

# tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.get_name() }}.")
#
# msg = tm.render(p=per)
#
# print(msg)

# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Сочи'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Ярославль'},
#     {'id': 5, 'city': 'Смоленск'}
# ]
#
# link = """<select name="cities">
# {% for c in cities %}
# {% if c.id > 3 %}
#     <option value="{{ c['id'] }}">{{ c['city'] }}</option>
# {% endif %}
# {% endfor %}
# </select>
# """
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)


# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300}
# ]
#
# # tpl = "Сумма: {{ cs | sum(attribute='price') }}"
# # tpl = "{{ cs | max(attribute='price') }}"
# # tpl = "{{ (cs | min(attribute='price')).model }}"
# # tpl = "{{ cs | random }}"
# tpl = "{{ cs | replace('model', 'brand') }}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# Макроопределение

# html = """
# {% macro input_func(name, value, type="text", size=40) %}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {% endmacro %}
#
# <p>{{ input_func('name', 'Введите имя') }}</p>
# <p>{{ input_func('psw', 'Пароль', 'password') }}</p>
# <p>{{ input_func('email', 'Электронная почта', 'email') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)


from jinja2 import Environment, FileSystemLoader

persons = [
    {"name": "Алексей", "year": 18, "weight": 78.5},
    {"name": "Никита", "year": 28, "weight": 82.3},
    {"name": "Виталий", "year": 33, "weight": 94.0}
]


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render(users=persons, title="About Jinja")

print(msg)



























