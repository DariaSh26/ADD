# 5 урок
from email.policy import default
from multiprocessing.managers import ListProxy
from textwrap import wrap

import a

# print(dir(list))                             # Добавление переменных в список
# a = [7, 9, 2, 1, 3, 8]
# print(a)
# a.append(5)
# print(a)
# a.extend([6, 7])
# print(a)
# a.insert(2, 8)
# print(a)
# from os import name


# s = []                                          # Добавление переменных в список
# n = int(input("Кол-во элементов списка: "))
# for i in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# print(s)


# a = [1, 2, 3]                                # Добавление переменных в список
# b = [11, 22, 33]
# c = []
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
#
# print(c)


# a = [7, 9, 2, 1, 3, 8]         #Удаление переменных в списке
# print(a)
# # del a[0]
# # print(a)
# # a[3:] = []
# # print(a)
# # a.remove(1)
# # print(a)
# # last = a.pop()
# # print(last)
# # print(a)
# last = a.pop(-2)
# print(last)
# print(a)

# a = [7, 9, 2, 1, 3, 8]
# print(a)
# # num = a.count(1)           #Сколько встречается какой то элемент
# ch = 7
# if ch in a:
#     num = a.index(ch)              # на каком индексе находится элемент
#     print(num)
# a.clear()
# print(a)

# a = [7, 9, 2, 1, 3, 8]
# print(a)
# new_list = a.copy()
# print(new_list)
# new_list.append(400)
# print(new_list)
# print(a)


# a = [7, 9, 2, 1, 3, 8]
# print(a)

# # a.reverse()    #развернуть список
# # print(a)
#
# lst = list(reversed(a))
# print(lst)
# print(a)


# a = [7, 9, 2, 1, 3, 8]
# print(a)
# a.sort(reverse=True)
# print(a)


# lst = ["Виталий", "Сергей", "Александр", "Анна"]
# print(lst)
# # lst.sort(key = len, reverse = True)
# new_lst = sorted(lst)
# print(new_lst)
# print(lst)


# import random
#
# print(random.random())
# print(random.randint(1, 9))
# print(random.randrange(1, 10))


# import random as rnd
#
# print(rnd.randint(1, 9))
# print(rnd.randrange(1, 10))


# from random import randrange, randint  #преимущественный вариант по размеру добавляемых элементов
#
# print(randint(1, 9))
# print(randrange(1, 10))


# from random import *    #тоже самое, но добавляет в документ * лишние данные и вес файла
#
# print(randint(1, 9))
# print(randrange(1, 10))


# import random as rnd
#
# # city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# # # print(rnd.choice(city_list))
# # # print(rnd.choices(city_list, k=3))
# # rnd.shuffle(city_list)
# # print(city_list)
#
# lst = [rnd.randint(1,10) for _ in range(10)]
# print(lst)


# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))


# import random
#
# lst = [random.randint(a:0, b:100) for _ in range(10)]     #код не работает, проверить. Здесь из списка ищется макс число и уберается из списка
# print(lst)
# maximum = max(lst)
# print("max =", maximum)
# lst.remove(maximum)
# lst.insert(0, maximum)
# print(lst)


# матрицы

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(matrix)
# print(len(matrix))
# print(matrix[1][2])


# =====================================

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(matrix)
# for row in range(len(matrix)):
#     # print(matrix[row])
#     for col in range(len(matrix[row])):
#         print(matrix[row][col], end="\t")
#     print()
# print()
# #=======================
# for row in matrix:
#     for col in row:
#      print(col, end ="\t)
#      print()


#
# import math
#
# print(math.sqrt(4))
# print(math.ceil(3.2))
# print(math.floor(3.8))
# print(math.pi)


# def hello(name, word):             #аргумент
#     print("Hello, ", name, ". Say ", word, sep="")
#
#
# hello("Irina", "hi")               #параметры
# hello("Ivan", "hello")


# def get_sum(a, b):
#     print(a + b)
#
# x = 2
# y  = 5
# get_sum(x, y)
# n = 3
# m = 6
# get_sum(n, m)


# def get_sum(a, b):
#     print("Сумма:", end=" ")
#     return a + b
#
# x = 2
# y  = 5
# res = get_sum(x, y)
# print(res)


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))


# def cube(a):
#     return a*a*a
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))


# def change(lst):
#     # last = lst.pop()   "1 способ
#     # first = lst.pop(0)
#     # lst.insert(0, last)
#     # lst.append(first)
#     lst[0], lst[-1] = lst[-1], lst[0]        #2 способ более короткий
#     return lst
#
#
# print(change([1,2,3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))


# 6 урок


# board = [" "] * 9   #[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# game_over = False
# player = "X"
#
#
#
# def show():
#     print(board[0] + " |" + board[1] + " |" + board[2])
#     print("- + - + -")
#     print(board[3] + " |" + board[4] + " |" + board[5])
#     print("- + - + -")
#     print(board[6] + " |" + board[7] + " |" + board[8])
#
# def check():
#     return (board[0] == board[1] == board[2] == player or
#             board[3] == board[4] == board[5] == player or
#             board[6] == board[7] == board[8] == player or
#             board[0] == board[3] == board[6] == player or
#             board[1] == board[4] == board[7] == player or
#             board[0] == board[4] == board[8] == player or
#             board[2] == board[4] == board[6] == player)
#
#
#
# while not game_over:
#     show()
#     move = int(input("\nХод" + player + " (1-9): ")) - 1
#
#     if board[move] == " ":
#         board[move] = player
#     else:
#         print("Занято")
#         continue
#
#     if check():
#         show()
#         print("\nПользователь " + player + "победил")
#         game_over = True
#     player = "0" if player == "X" else "X"


# 7 урок
#
#
# import random
#
#
# def run(a, b):
#     return tuple(random.randint(a, b) for _ in range(10))
#
#
# tpl1 = run(a:0, b:5)
# print(tpl1)
# tlp2 = run(-5, b:0)
# print(tlp2)
#
# tpl3 = tpl1 + tlp2
# print(tpl3)
# print("0 =",tpl3.count(0))


# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
#
# print(countries, end="\n\n")
#
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана: ", countryName, ", население = ", countryPopulation, sep="")
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород: ", cityName, ", население = ", cityPopulation, sep="")


# tpl = tuple(input("Введите данные: "))
# print(tpl)
#
# lst = []
# for item in tpl:
#     if item not in lst:
#         lst.append(item)
#
# for item in lst:
#     print("Количество:", item, "=", tpl.count(item))


# s = {"banana", "apple", "mango", "banana", "apple"}
# print(s, type(s))
# for x in s:
#     print(x)


# a = set("Hello")
# print(a, type(a))

# s = {x * x for x in range(10)}
# print(s)

# t = {"red", "green", "blue" }
# print("green" in t)
# print("yellow" in t)


# t = ["ab_1", "ac_2", "bc_1", "bc_2"]
# # a = [i for i in t if "a" not in i]
# # a = {'А' + i [1:] if i [0] == "a" else "B"  + i[1:] for i in t}
# a = ['А' + i[1:] if i[0] == "a" else "B"  + i[1:] for i in t if i[1] == "c"]
# print(a)


# a = {0, 1, 2, 3}
# print(a)
# a.add(4)
# print(a)


# users = {"Tom", "Bob", "Alice"}
# print(users)
# # users.remove("Tom")
# # print(users)
# # users.remove("Ann")   # KeyError
# # print(users)
#
# # user = "Ann"
# # if user in users:
# #     users.remove(user)
# # print(users)
#
# # users.discard("Ann")
# # print(users)
#
# users.pop()
# print(users)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)    # с = a | b - тоже самое
# print(c)
# a |= b            # тоже самое что выше
# print(a)

#
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
# count = len(s)
# print("Кол-во элементов:", count)
# print("MIN: ", min(s))
# print("MAX: ", max(s))


# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# # print(s)
# for i in s:
#     print(i, end=" ")
# print()
# print(s1)
# print(s2)

# s1 = "Python"
# s2 = "Programming language"
# a = list(set(s1) - set(s2))
# print(a)
# for x in a:
#     print(x, end=" ")


# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
#
# # print(b <= a)
# print(a <= b)
# print(a < b)
# print(a >= b)
# print(a > b)


# drawing = {"марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
#
# one_hobby = drawing ^ music
# print("Один кружок:", one_hobby)
#
# both_hobbies = drawing & music
# print("Два кружка:", both_hobbies)
#
# drawing -= both_hobbies
# print(drawing)


# s = frozenset([1, 2, 3, 4, 5])
# s = frozenset({"hello", "world"})
# print(s)


# 8 урок   словарь


# d = {0: "text", "one": 45, (5,4): "Кортеж", "список": [2, 4, 5], True: 1, False: 0, 1: 45}
# print(d)
#
# del d["one"]
# print(d)


# print("список" in d)
# print("список" in d)
# print(d[0])
# print(d[True])
# print(d[1])
# print(d[(5, 4)])
# print(d["список"][1])

#
# s = {"g", "w", "e", "g"}
# print(s)
#
#
# d = {"one": 10, "two": 20, "three": 30}
# print(d, type(d))
#
#
# lst = [1, 2, 3]
# print(tuple(lst))
#
# lst = (
#     ("one", 1), ("two", 2), ("three", 3)
# )
# print(dict(lst))


# d = {a: a for a in range(10)}
# print(d)
#
# d = {a: a ** 2 for a in range(2, 10)}
# print(d)

# d = {"one": 10, "two": 20, "three": 30}
# print(d)
# print(d["two"])
# d["two"] = 2 ** 4
# print(d)


# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
#
# res = 1
# for key in d:
#     res *= d[key]
#
# print(res)


# d = dict()                       # более длинный вариант
# d[1] = input(" ->")
# d[2] = input(" ->")
# d[3] = input(" ->")
# d[4] = input(" ->")
# print(d)

# d = {i: input(" ->")for i in range(1, 5)}     # более корткий вариант
# print(d)
# delete = int(input("Какой элемент исключить: "))       #  удалить элемент
# del d[delete]
# print(d)


# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-467K', 3, 8500],
#     '3': ['AMD FX-i3-6330', 6, 3700],
#     '4': ['Pentium G63220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ")", goods[i][0], " - " , goods[i][1], "шт. по ", goods[i][2], "руб",  sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n] [1] += count
#                     break
#                 except ValueError:
#                     print("Значение некорректное. Введите число")
#         else:
#             print("такого ключа не существует")
#     else:
#         break
#
# for i in goods:
#     print(i, ")", goods[i][0], " - " , goods[i][1], "шт. по ", goods[i][2], "руб",  sep="")


# d = {"one": 1, "two": 2, "three": 3}
#
# # print(d.keys())    dict_keys(['one', 'two', 'three'])
# # print(d.values())   dict_values([1, 2, 3])
# # print(d.items())   dict_items([('one', 1,) ('two', 2), ('three', 3 )])
#
# # for key, value in d.items():
# #     print(key, value)
#
# # value = d["four"]
# value = d.get (key: "four", default: "Такого ключа нет")
# print(value)


# d = {"one": 1, "two": 2, "three": 3}
# print(d)

# item = d.pop("three")   # 3 метода удаления
# print(item)
# print(d)

# item = d.popitem()
# print(item)
# print(d)

# d.clear()
# print(d)


# item = d.setdefault("four", 4)   # добавляем в конец словаря значение
# print(item)
# print(d)


# d1 = dict.fromkeys(['a', 'b', 'c', 'd'], 100)
# print(d1)


# d = {"one": 1, "two": 2, "three": 3}
# print(d)

# d2 = d.copy()
# print("d =", d)
# print("d2 =", d2)
#
# d["two"] = 5
# d2["three"] = 6
#
# print("d =", d)
# print("d2 =", d2)


# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = {"one": 1, "two": 2, "three": 3}
# d.update({'d': 4, 'e': 5, 'f': 6})
# d.update(d2)
# d.update([('r', 7), ('g', 9)])
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = {"one": 1, "two": 2, "three": 3}
#
# d3 = d| d2
# print(d3)


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': "New York"}
#
# # new_d = dict()
# # new_d["name"] = d.pop("name")
# # new_d["salary"] = d.pop("salary")
# new_d = {"name": d.pop("name"), "salary": d.pop("salary")}
# print(d)
# print(new_d)


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': "New York"}
# d["location"] = d.pop("city")
# print(d)

# d = {
#     "first": {
#         1: "one",
#         2: "two",
#         3: "three",
#     },
#     "second": {
#         4: "four",
#         5: "five",
#     }
# }
# print(d)
# # for x in d:
# #     print(x)
# #     for y in d[x]:
# #         print("\t", y, ":", d[x] [y], sep="")
#
# for x, y in d.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ":", j, sep="")


# d = {"one": 1, "two": 2, "three": 3}           # генератор словарей, поменять местами
# print(d)
#
# new_d = {v: k for k, v in d.items()}
# print(new_d)


# 9 урок


# lst = [1, 2, 3, 4]
# d = {k: int(input("->")) for k in lst}
# print(d)


# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
# print(list(zip([1,2,3])))


# one = {'name': 'Igor', 'surname': 'Vetrov', 'age': 26}               #распаковка кортежей
# two = {'name': 'Irina', 'surname': 'Petrova', 'age': 20}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)
#
# print(list(zip(one.items(), two.items())))


# распаковка словаря

# one = {'one': 1, 'two': 2}
# two = {'three': 3, 'four': 4}
# print({**one, **two})

# a = [1,2,3]
# b = [*a, 4,5,6]
# print(b)


# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1,2,3, 'abc'))


# def average(*args):
#     return sum(args) / len(args)
#
#
# print(average(1,2,3,4,5,6))
# print(average(1,2,3))


# def average(*args):
#     aver = sum(args) / len(args)
#     print(aver)
#     res = []
#     for num in args:
#         if num < aver:
#             res.append(num)
#     return res
#
#
# print(average(1,2,3,4,5,6,7,8,9))
# print(average(3,6,1,9,5))


# def func(a, *args):
#    return a, args
#
#
# print(func(1))
# print(func(1, 2, 3))

#
# def print_data(student, *scores):
#     print("Student Name:", student)
#     for score in scores:
#         print(score)
#
#
# print_data( student:"Igor", *scores:100, 95, 88, 92, 99)
# print_data(sudent: "Marina", *scores:96, 20, 33, 56)
# print_data("Irina")


#
# def func(a, b, *args, e: int = 0, **kwargs):           #некорректно работает
#     return a, b, args, kwargs, e
#
#
# print (func(a:1, b:2, *args:3, 4, 5, e = 100, c=6, d=7))


# name = "Tom"  # глобальная переменная
#
#
# def hi():
#     surname = "Johnson"   # локальная переменная
#     print("Hello", name)
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()


# import builtins
#
# names = dir(builtins)
#
# for name in names:
#     print(name)


# def func(a):
#     one = 100
#     x = 2 #  область объемлющих функций
#
#     def inner():
#         one = 1000
#         print("x =", x)
#         return one
#
#     return inner()
#
#
# print(func(5))

# who = "World"
#
# def outer(who):
#     global who
#     who = "Mari"
#
#     def inner():
#         print("Hello", who)  #3
#
#     inner()   #2
#
# outer()    #1
# print(who)


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner()
#         nonlocal a, b
#         a = a1+ a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(a1:2, b1:3, a2:-1, b2:4))    # [1,7]


# замыкание

# def outer(n):  # 1
#     def inner(x): # 10
#         return x + n
#
#     return inner
#
#
# add1 = outer(1)
# print(add1(10))
#
# add2 = outer(2)
# print(add2(10))
#
# print(outer(3)(10))


# def outer():
#     a = 1
#     b = 'line'
#     c = [1,2,3]
#
#     def inner():
#         nonlocal a, b
#         c.append(4)
#         a += 1
#         b = b + "_new"
#         return a, b, c
#
#     return inner
#
#
# func = outer()
# print(func())


#  ДЗ


# def func(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count +=1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
#
# res1()


# Анонимные функции, lambda - выражения
# print((lambda x, y: x + y) (1,2))
# print((lambda n, m: n ** 2 + m ** 2) (2,5))


# print((lambda a=1, b=2, c=3: a + b + c)(10,20, 30))
#
# #
# summ = lambda a = 1, b = 2, c= 3: a + b + c
# print(summ(10,20,30))

# print((lambda *args: sum(args))(1,2,3,4))


# tpl = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in tpl:
#     print(t("abc"))


# def outer(n):             # 1 способ
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(42)
# print(f(0))
#
#
# def outer(n):                   # 2 способ, короткий способ
#     return lambda x: x + n
#
#
# f = outer(42)
# print(f(0))
#
#
# outer = lambda n: lambda x: x + n    # 3 способ
#
# f = outer(42)
# print(f(0))
#
# print((lambda n: lambda x: x + n)(42) (0))     # 4 способ


# def values(i):                   # lambda выражение в кортеже
#     return i[1]
#
# d = {'b': 15, 'c': 5, 'a': 10}
# lst = list(d.items())
# print(lst)
# # lst.sort(key=lambda i: i[1], reverse=True)
# lst.sort(key=values, reverse=True)
# print(lst)
# print(lst)
# print(dict(lst))


# lst = [                                     # lambda выражение в списке
#     lambda x, y: x + y,
#     lambda x, y: x - y,
#     lambda x, y: x * y,
#     lambda x, y: x / y
# ]
#
#
# print(lst[0](x=5, y=12))
# print(lst[1](x=12, y=5))


# d = {                                                # lambda выражение в словаре
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
# }
#
# d[3]()


#
# print((lambda a, b: a if a > b else b) (15, 23))

# print((lambda a, b, c: min(a, b, c))(9, 8, 5))  # Найти мин значение


# map(func, *iterables)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# print(list(map(mult, lst)))


# map(func, *iterables)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
#
# print(list(map(lambda t: t * 2, lst)))


# old = ['5', '4', '7', '8']
# print(old)
# print(list(map(int, old)))


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# print(list(map(lambda x, y: (x, y), st, num)))


# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
#
# print(tuple(filter(lambda s: len(s) == 3, t)))


# lst = [66, 98, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(lambda s: s > 75, lst)))


# Декораторы

# def hello ():
#     return "Hello, I am func 'hello'"
#
# def super_func(func):
#     print("Hello, I am super_func")
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

#
# def my_decorator(func):
#     def wrapper():
#         print("Code before")
#         func()
#         print("Code after")
#     return wrapper
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
# test = my_decorator(func_test)
# test()


#
# def my_decorator(func):           # декорирующая функция
#     def wrapper():
#         print("*" * 30)
#         func()
#         print("*" * 30)
#     return wrapper
#
# @my_decorator              # декоратор
# def func_test():           # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator              # декоратор
# def hello():
#     print ("Hello, I am func 'hello'")
#
#
# func_test()
# hello()


# def circle(fn):
#     def wrap():
#         return "(" + fn() + ")"
#     return wrap
#
#
# def angle(fn):
#     def wrap():
#         return "<" + fn() + ">"
#     return wrap
#
#
# @angle
# @circle
# def expression():
#     return '5 + 2'

#
# print(expression())


#
# def cnt(fn):
#     count = 0
#
#     def wrapper():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrapper
#
#
# @cnt
# def hello():
#     print("hello")
#
#
# hello()
# hello()
# hello()


# def args_decorator(func):
#     def wrap(arg1, arg2):
#         func(arg1, arg2)
#         print("данные:", arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def full_name(name, surname):
#     print("Меня зовут", name, surname)
#
#
# full_name("Ирина", "Ветрова")


# def args_decorator(func):
#     def wrap(*args, **kwargs):
#         print("args", args)
#         print("kwargs", args)
#         func(*args, **kwargs)
#
#
#     return wrap
#
#
# @args_decorator
# def full_name(a, b, c, study = "Python"):
#     print(a, b, c, "изучают", study, end="\n\n")
#
#
# full_name("Ирина", "Борис", "светлана", study="JavaScript")
# full_name("Владимир", "Екатерина", "Виктор")


# def multiply(arg):
#     def decor(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return decor
#
# @multiply(3)
# def return_num(num):
#     return num


# print(return_num(5))


#
# def avg(fn):
#     def wrap(*args):
#         print("Среднее арифметическое:", args, "=", fn(*args) / len(args))
#
#     return wrap
#
#
#
# @avg
# def summa(*args):
#     print("Сумма чисел:", args, "=", sum(args))
#     return sum(args)
#
#
# summa(2,3,3,4)


# 11 урок


#
# print(bin(18))    # 0b10010
# print(oct(18))    # Oo22
# print(hex(18))    # 0x12


# g = 'Pyt'
# w = 'hon'
# e = g + w
# print(e)
# # print(e * 3)
# # print('y' in e)
# # print('a' in e)
# # print(e[1])
# # print(e[1:5])
# # print(e[1:5:2])
# print(e[::-1])

# print("C:\\folder\\file.py")
# print(r"C:\folder\file.py")


# name = "Дмитрий"
# age = 25
#
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")

# x = 10
# y = 5
# print(f"{x} * {y} / 2 = {x * y / 2}")
# print(f"{x=}, {y=}")


# mas = [4, 5, 7, 8]
# print(f"{mas[1]}")

#
# print(f"13 / 3 = {round(13 / 3, 2)}")
# print(f"13 / 3 = {13 / 3:.2f}")


# dir_name = "folder"
# file_name = "file.py"
# print(fr"home\{dir_name}\{file_name}")

# a = ("Hello "
#      "World")
# print(a)
#
# b = """Hello
# World"""
# print(b)
#
# d = '''Hello
# World'''
# print(d)

# def square(x):
#     """Принимает число n, возвращает квадрат числа n"""  # чтобы работал как документация, и необходимо чтобы была 1 строкой
#     return x ** 2
#
#
# print(square(3))
# print(square.__doc__)
# # print(max.__doc__)
# print(len.__doc__)

# import math
#
#
# def cylinder(r, h):
#     """
#     вычисляет плошадь цилиндра.
#
#     вычисляет плошадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r * h)
#
#
# print(cylinder(2, 5))
# print(cylinder.__doc__)


# print(ord('a'))   # 97
# print(ord('ю'))  # 1102

# while True:
#     n = input("->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# my_str = "Test string for me"
# arr = [ord(x) for x in my_str]
# print("ASCII коды:", arr)

#
# def fio(name):
#     print(f"{name[0]}")


# my_str = "Test string for me "
# arr = [ord(x) for x in my_str]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое", arr)
# arr += [ord(x) for x in input("->") [:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) -1)
# arr.sort(reverse=True)
# print(arr)

#
# print(chr(97))


#
# from random import randint
#
# shortest = 6
# longest = 12
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     random_length = randint(shortest, longest)
#     res = ""
#     for i in range(random_length):
#         random_char = chr(randint(min_ascii, max_ascii))
#         res += random_char
#     return res
#
#
# print("Ваш случайный пароль:", random_password())


# print(dir(str))
#
# s = "hello, WORLD! i am learning Python."
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())

# print(s.count("l", 3, 10))
# print(s.lower(). count("l"))

# print(s.find("l"))
# print(s.rfind("l"))
#
# print(s.index("l"))
# print(s.rindex("l"))

#
# print(s.endswith("on"))     # для проверки типа данных
# print(s.startswith("WORLD", 7))

#
# print("abc123". isalnum())   #True
# print("abc". isalnum())     #False

# print("gww".isalpha())   # проверяет буквы
#
# print("122".isdigit()) #проверяет цифры

# print('abc!@@122Q'.islower())
# print('abcghgh13123'.islower())
#
# print("ABC@#$1223".isupper())

# print("py".center(10, "-"))

# print("    py".lstrip())
# print("p y    ".rstrip())
# print("      p y     ".strip())

#
# print("https://www.python.org/".strip("/:pthsorg"))

#
# s = "Я изучаю Nython.  мне нравится Nython. Nython очень интересный язык программирования"
# print(s.replace("Nython", "Python", 2))

# s = "-"
# seg = ("a", "b", "c", "d")
# print(s.join(seg))
#
# print("..".join(["1", "2"]))
#
# print(":".join("Hello"))

#
# print("Строка разделенная пробелами".split())
# print("www.python.org".split("."))
#
# a = input("-> ").split()
# print(a)


# def fio(name):
#     print(f"{name[0]} {name[1][0]}.{name[2][0]}.")
#
# st = input("ВВедите ФИО: ").split()
# print(st)
# fio(st)

# 12 урок   работа с файлами

# f = open("text.txt", "r")
# f = open(r"C:\Users\daria\OneDrive\Рабочий стол\ADD\text.txt", "r")
# print(f)
# print(*f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# f.close()      # закрыть файл
# print(f.closed)     # открыт ли файл?


# f = open("text.txt", "r")
# print(f.read(3))
# print(f.read())
# f.close()


# f = open("text.txt")
# try:
#     print(f.read())
# finally:
#     f.close()


# f = open("test.txt")
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open("test.txt")
# print(f.readlines(26))
# print(f.readlines())
# f.close()


# f = open("test.txt")
# for line in f:
#     print(line)
# f.close()


# f = open("xyz.txt", "w")
# f. write("Hello \nWorld!\n")
# f.close()

# f = open("xyz.txt", "a")
# f. write("New text.\n")
# f.close()

#
# f = open("xyz.txt", "w")
#
# f.close()


# f = open("xyz.txt", "a")
#
# f.close()


# lines = ["This is line 1\n", "This is line 2\n"]
#
# f = open("xyz.txt", "a")
# f.writelines(lines)
# f.close()


# lines = [str(i) + "\t" for i in range(1, 20)]
# print(lines)
# f = open("xyz.txt", "w")
# f.writelines(lines)
# f.close()


# f = open("text2.txt","w")
# f.write("Замена строки в текстовом файле; \nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()
#
# f = open("text2.txt","r")
# read = f.readlines()
# f.close()
#
# print(read)
# read[1] = "Hello World!\n"
# print(read)
#
#
# f = open("text2.txt","w")
# f.writelines(read)
# f.close()


# f = open("text.txt","r")
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()


# f = open("text223.txt","a+")
# f.write("Hello \nWorld!\n")
# print(f.readlines())
# f.close()


# file_name = "res.txt"
# lst = [4.5, 2.8, 1.0, 0.3, 4.3, 7.777]
#
# def get_line(lt):
#     lt = map(str, lt)
#     return " ".join(lt)
#
#
# with open(file_name, "w") as f:
#     f.write(get_line(lst))
#
# print("Done!")
#
# with open(file_name, "r") as f:
#     nums = f.read()
#
# print(nums)
# nums_list = list(map(float, nums.split()))
# print(nums_list)
# print(sum(nums_list))


# def longest_words(file):
#     with open(file, encoding ="UTF-8") as f:
#          w = f.read().split()
#          print(w)
#          max_length = len(max(w, key=len))
#          res = [word for word in w if len(word) == max_length]
#          if len(res) == 1:
#              return res[0]
#          return res
#
#
# print(longest_words("text.txt"))

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open("one.txt","w") as f:
#     f.write(text)
#
# read_file = "one.txt"
# write_file = "two.txt"
#
# with open(read_file, "r") as fr, open(write_file, "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)


# import pickle
#
# # file_name = "basket.txt"
#
# shop_list = {"фрукты": ["яблоки", "манго"],
#              "овощи": ("Морковь", "лук"),
#              "бюджет": 1000}
# #
# # with open(file_name, "w") as f:
# #     pickle.dump(shop_list, f)
# #
# # with open(file_name, "rb") as f:
# #     print(pickle.load(f))
#
# shop = pickle.dumps(shop_list)
# print(shop)
#
# load_shop = pickle.loads(shop)
# print(load_shop)


# import json
#
# data = {
#     'name': 'Olga',
#     'age': '20',
#     20: None,
#     True: True,
#     None: False,
#     "list": (5, 8, 9, 7),
# }

# with open('data_file.json', 'w') as f:
#     json.dump(data, f, indent=4)
#
# with open('data_file.json', 'r') as f:
#     data = json.load(f)
#
# print(data)
#
# json_string = json.dumps(data)
# print(json_string, type(json_string))
#
# data1 = json.loads(json_string)
# print(data1, type(data1))


# 13 урок


#
#
# import json
# from random import choice
#
#
#
# def gen_persons():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#     nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {'name': name, 'tel': tel}
#     return person  # {"name": " ....", "tel": "..."}
#
#
# def write_json(person_dict):   # {"name": " ....", "tel": "..."}
#     try:
#         data = json.load (open('persons.json', "r"))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)   # [{"name": " ....", "tel": "..."}, {"name": " ....", "tel": "..."}]
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())


#
#
#
# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# # print(type(todos))
# # print(todos[0])
# filter_todos = []
#
# for todo in todos:
#     if todo['completed']:
#         filter_todos.append(todo)
#
# # print(filter_todos, len(filter_todos))
# with open('todos.json', 'w') as f:
#     json.dump(filter_todos, f, indent=2)
#
# with open('todos.json') as f:
#     data = json.load(f)
#     print(data, len(data))


#
# import csv

# with open("data.csv") as f:                                        # 1
#     file_reader = csv.reader(f, delimiter=';')
#     count = 0
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {",".join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")


# with open("data.csv") as f:                                         # 2
#     file_reader = csv.DictReader(f, delimiter=';')
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {",".join(row)}")
#         print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1

# import csv
# with open("data.csv") as f:
#     field_name = ["Имя", "Профессия", "Год рождения"]
#     file_reader = csv.DictReader(f, delimiter=';', fieldnames=field_name)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {','.join(row)}")
#         print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1


# import csv

# with open("students.csv", "w") as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\n')
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", 9, 15])
#     writer.writerow(["Саша", 5, 12])
#     writer.writerow(["Маша", 11, 18])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('data_new.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)

#
# with open('student_1.csv', 'w') as f:
#     names = ["Имя", "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=';', fieldnames=names, lineterminator='\r')
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Саша", "Возраст": 6})
#     file_writer.writerow({"Имя": "Маша", "Возраст": 15})
#     file_writer.writerow({"Имя": "Вова", "Возраст": 14})


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
#
# with open("file_data.csv", "w") as f:
#     writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=';', lineterminator='\r')
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)
#


# import csv
# import requests
#
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = response.json()
#
# with open('todos1.csv', 'w', newline= '') as f:
#     names = ["userId", "id", "title", "completed"]
#     file_writer = csv.DictWriter(f,  delimiter=";", fieldnames=names, lineterminator='\r')
#     file_writer.writeheader()
#     file_writer.writerows(todos)
#
# print()


# import random
# print(2.1 == random.uniform(2.1, 2.1))


# База данных


# import sqlite3


# conn = sqlite3.connect('profile.db')
# cur = conn.cursor()
#
# conn.close()
#
# with sqlite3.connect('profile.db') as con:
#     cur = con.cursor()
#     # cur. execute('''CREATE TABLE IF NOT EXISTS users (
#     #      id INTEGER PRIMARY KEY AUTOINCREMENT,
#     #      name TEXT NOT NULL,
#     #      summa REAL,
#     #      date BLOB
#     # )''')
#     cur.execute("DROP TABLE IF EXISTS users")   # удалить бд


# import sqlite3
#
# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
# cur.execute('''CREATE TABLE IF NOT EXISTS person(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB DEFAULT "+79990000000",
#     age INTEGER NOT NULL CHECK (age >= 0 AND age <= 100),
#     email TEXT UNIQUE NOT NULL
# )''')
# cur.execute('''
# ALTER TABLE person_table
# ADD COLUMN address TEXT
# ''')
# cur.execute('''
# ALTER TABLE person_table
# ADD COLUMN surname TEXT NOT NULL DEFAULT "fio"
# ''')

# cur.execute('''
# ALTER TABLE person_table
# RENAME COLUMN address TO home_address
# ''')

# cur.execute('''
# DROP TABLE person_table
# ''')


# import sqlite3
#
# with sqlite3.connect('db_3.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT *
#         FROM T1
#         ORDER BY FName
#         LIMIT 2,5;
#         """)
#
#
#     res1 = cur.fetchone()
#     print(res1)
#
#     res2 = cur.fetchmany(2)
#     print(res2)
#
#
#     res = cur.fetchall()
#     print(res)
#
# for res in cur:
#     print(res)


# import sqlite3           # создание таблицы
#
# with sqlite3.connect('people.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS companies (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL
#     )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER,
#         company_id INTEGER DEFAULT 1,
#         FOREIGN KEY (company_id) REFERENCES companies (id) ON DELETE SET DEFAULT
#     )""")


#
# import sqlite3    # создание таблицы
#
# with sqlite3.connect('people.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS books(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         count_page INTEGER NOT NULL CHECK (count_page > 0),
#         price REAL CHECK (price > 0)
#     )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS author(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER CHECK (age > 16)
#     )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS author_books(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         books_id INTEGER NOT NULL,
#         author_id INTEGER NOT NULL,
#         FOREIGN KEY(books_id) REFERENCES books(id),
#         FOREIGN KEY(author_id) REFERENCES author(id)
#     )""")


# import sqlite3
#
# with sqlite3.connect('people.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS student(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             surname TEXT NOT NULL,
#             name TEXT NOT NULL,
#             patronymic TEXT NOT NULL,
#             count_page INTEGER NOT NULL CHECK (count_page > 0),
#             group INTEGER NOT NULL
#         )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS groups(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         group_name  TEXT NOT NULL
#     )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS association(
#         lesson_id INTEGER NOT NULL,
#
#     )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS author_books(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             books_id INTEGER NOT NULL,
#             author_id INTEGER NOT NULL,
#             FOREIGN KEY(books_id) REFERENCES books(id),
#             FOREIGN KEY(author_id) REFERENCES author(id)
#         )""")
#
#
#
#
#
#     with sqlite3.connect('people.db') as connection:
#         cur = connection.cursor()
#         cur.execute('''CREATE TABLE IF NOT EXISTS student (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             surname TEXT,
#             name TEXT,
#             patronymic TEXT,
#             age INTEGER,
#             [group] INTEGER NOT NULL,
#             FOREIGN KEY ([group]) REFERENCES groups (id)
#         )''')
#
#         cur.execute('''CREATE TABLE IF NOT EXISTS groups (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             group_name TEXT
#         )''')
#
#         cur.execute('''CREATE TABLE IF NOT EXISTS association (
#             lesson_id INTEGER NOT NULL,
#             group_id INTEGER NOT NULL,
#             FOREIGN KEY (lesson_id) REFERENCES lessons (id)
#             FOREIGN KEY (group_id) REFERENCES groups (id)
#         )''')
#
#         cur.execute('''CREATE TABLE IF NOT EXISTS lessons (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             lesson_title TEXT
#         )''')


# import sqlite3

# auto = [
#     ('BMW', 54000),
#     ('Shevpolet', 54000),
#     ('daewoo', 38000),
#     ('Citroen', 529000),
#     ('Honda', 33000)
# ]
# with sqlite3.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )''')
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price +100;
#     """)

# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

# cur.executemany("INSERT INTO cars VALUES (NULL,?,?)", auto)

#
# for car in auto:
#     cur.execute("INSERT INTO cars VALUES (NULL,?,?)", car)

# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
# cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")


# con.commit()
# con.close()


# import sqlite3
# con = None
# try:
#     con = sqlite3.connect('cars.db')
#     cur = con.cursor()
#     cur.executescript('''CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#         );
#         BEGIN;
#         INSERT INTO cars VALUES (NULL, 'Renault', 22000);
#         UPDATE cars SET price = price + 100;
#         ''')
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
#  with sqlite3.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.executescript('''CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#          name TEXT, tr_in INTEGER, buy INTEGER
#          )''')
#
#     cur.executescript("INSERT INTO cars VALUES (NULL, 'Запорожец', 1000)")
#     last_id = cur.lastrowid
#     by_car_id = 2
#     cur.execute('INSERT INTO cost VALUES ("Федор", ?, ?)', (last_id, by_car_id))


# import sqlite3    переделать
#
# with sqlite3.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.executescript('''CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT,
#         tr_in INTEGER,
#         buy INTEGER
#     )''')
#
# cur.execute("INSERT INTO cars VALUES (NULL, 'Запорожец', 1000)")
#
# last_id = cur.lastrowid
# by_car_id = 2
# cur.execute('INSERT INTO cost VALUES ("Федор", ?, ?)', (last_id, by_car_id))


# import sqlite3
#
# with sqlite3.connect('cars.db') as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript('''CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )''')
#
#     cur.execute("SELECT model, price FROM cars")
#     # for row in cur:
#     #     print(row[1])
#     for row in cur:
#         print(row["model"], row["price"])
#
#     # row = cur.fetchone()
#     # print(row)
#     #
#     # print(cur.fetchmany(5))
#     #
#     # print(cur.fetchall())


# создание таблицы с изображением
# import sqlite3
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
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#         return True
#     except IOError as e:
#         print(e)
#         return False
#
# with sqlite3.connect('cars.db') as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#
#     cur.executescript('''CREATE TABLE IF NOT EXISTS users (
#          name TEXT,
#          ava BLOB,
#          score INTEGER
#         )''')
#
#     # img = read_ava(1)
#     # if img:
#     #     binary = sqlite3.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES ('Федор',?,1000)", (binary,))
#
#
#     cur.execute("SELECT ava FROM users LIMIT 1")    # ("бинарный код")
#     img = cur.fetchone() ["ava"]
#     write_ava("out.png", img)


###############################

# import sqlite3
#
# with sqlite3.connect('cars_new.db') as con:
#     cur = con.cursor()
#
#     # with open("sql_dump.sql", "w") as f:
#     #     for sql in con.iterdump():
#     #         f.write(sql)
#
#     with open("sql_dump.sql", "r") as f:   #восстановить таблицу
#         sql = f.read()
#         cur.executescript(sql)


# print("Изменения после коммита")

# print("Hello World")






#======================================
# Библиотека Numpy

# import numpy as np
#
# lst = [1, 2, 3, 4, 5]
# print(lst * 2)

# arr = np.array([1, 2, 3, 4, 5])   # одновременный массив
# print(arr)
#
#
# arr2 = np.array([[1, 2, 3, 11, 12, 13], [4, 5, 6, 14, 15, 16]])  # двумерный массив
# print(arr2)
#
# print(arr * 2)
# print(arr2 * 2)


# # количество измерений массива
# print(arr.ndim)
# print(arr2.ndim)

# количество строк и столбцов
# print(arr.shape)
# print(arr2.shape)

# общее количество элементов
# print(arr.size)
# print(arr2.size)


# print(arr2[0, 2])
# print(arr2[:, 0])
# print(arr2[0, 1:4:2])
# print(arr2[1, 0:-1:2])

# arr2[0,0] = 50
# print(arr2)

# arr2[0, :] = [0, 0, 0, 1, 1, 1]
# print(arr2)

# zeros = np.zeros((3,4), dtype="int32")
# print(zeros)
#
# ones = np.ones((2,3))
# print(ones)


# mas = np.full((2,3), 5)                      # в результате будет [5 5 5]
# print(mas)                                                        [5 5 5]


# d = np.random.randint(-5,10, size=(3,4))     # формируются случайные числа
# print(d)

# d = np.linspace(0,10,5)                      # получение массива с равномерно распредлен числами, вещественные числа
# print(d)

# d = np.arange(0,10,3)                        # получение массива в заданном диапазоне [0 3 6 9]
# print(d)


# arr = np.arange(1,13)                        # получение одномерного массива
# print(arr)
#
# two = np.reshape(arr,(3,4))                 # предыдущий массив преобразовать в двумерный массив
# print(two)

# ==================
# arr1 = np.array([1, 2, 3])            # объеденение массивов по горизонтали и вертикали
# arr2 = np.array([4, 5, 6])
#
# hstack = np.hstack((arr1, arr2))      # одномерный массив по горизонтали
# print(hstack)
#
# vstack = np.vstack((arr1, arr2))      # двумерный массив
# print(vstack)
# =========================


# arr1 = np.array([1, 2, 3, 4])
# print(arr1)
# print(arr1 + 3)                    #  к массиву добавили +3
# print(arr1 - 2)
# print(arr1 * 2)
# print(arr1 ** 2)
# ============================


# a = np.array([[1,2], [3,4]])
# b = np.array([[2,2], [2,2]])
#
# print(a + b)
# print(a * b)
# =============================


# a = np.array([[1,2,3], [4,5,6]])
# print(a)

# total = a.sum()             # общая сумма всех элементов массива
# print(total)
#
# col = a.sum(axis=0)          # возращает сумму столбцов (1+4, 2+3б 3+9)
# print(col)                         axis - первая ось соответствует вниз как по строкам, но идет по стобцам
#
# row = a.sum(axis=1)         # получили сумму в пределах строки
# print(row)
# =======================================

# a = np.array([[1,2,3], [4,5,6]])
# print(a)

# mean_all = a.mean()             # среднее арифметическое полностью по всем элементам массива (сложились все элементы и разделились на 6)
# print(mean_all)
#
# mean_0 = a.mean(axis=0)        # среднее ариф- ое 1+4 / 2 = 2,5, 2+5/2 = 3,5, 3+6/2 = 4,5 (по столбцу)
# print(mean_0)
#
# mean_1 = a.mean(axis=1)       # среднее арифм по строке
# print(mean_1)
# ==============================


# a = np.array([[1,2,3], [4,5,6]])
# print(a)

# min_all = a.min()
# print(min_all)

# min_0 = a.min(axis=0)        # выбирает мин значение по оси, результат будет [1, 2, 3] в пределах столбцов
# print(min_0)

# min_1 = a.max(axis=1)       # в пределах строк
# print(max_1)
# ==================================
#
# a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a)
#
# arg_max = a.argmax()       # индекс на котором находится макс значение
# print(arg_max)

# arg_0 = a.argmax(axis=0)   # индекс по оси столбца
# print(arg_0)

# arg_1 = a.argmin(axis=1)   # индекс по строке
# print(arg_1)
# ======================================


# a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a)

# prod_all = a.prod()            # находить произведение элементов
# print(prod_all)
#
# prod_0 = a.prod(axis=0)
# print(prod_0)
#
# prod_1 = a.prod(axis=1)
# print(prod_1)
#
# var_all = a.var()             # определение дисперсии (в теме анализ есть пункт дисперсия)
# print(var_all)
#
# var_0 = a.var(axis=0)
# print(var_0)
#
# var_1 = a.var(axis=1)
# print(var_1)
# ===========================================


# arr1 = np.array([1,5,20])          # нахождение медианы
# print(arr1)
# print(np.median(arr1))

# arr1 = np.array([2, 4, 1, 10])
# print(arr1)
# print(np.median(arr1))

# ===============================

# arr = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])    # стандартное отклонение
# # arr = np.array([2, 4, 4, 4, 6])
# print(arr)
# print(np.std(arr, axis=0))
# ================================================


# анализ данных по зп сотрудников компании

# salaries = np.array([50, 23, 60, 26, 19, 43, 26, 64, 60, 45, 26, 57, 54])
# print(salaries)
#
# mean_salary = np.mean(salaries)
# print(f"Средняя зарплата: {mean_salary:.2f}")     # .2f - округление
#
# max_salary = np.max(salaries)
# min_salary = np.min(salaries)
# print(f"Максимальная зарплата: {max_salary}")
# print(f"Минимальная зарлпта: {min_salary}")
#
# std_salary = np.std(salaries)
# print(f"Стандартное отклонение зарплаты: {std_salary:.2f}")
#
# above_mean = salaries[salaries > mean_salary]
# print(f"Зарплаты выше среднего: {above_mean}")


# ========================================================
# Анализ продаж магазина за последний месяц

# product_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
# prices = np.array([10.99, 20.99, 15.49, 25.49, 5.99, 12.99, 7.99, 30.99, 18.99, 9.99])
# quantities  = np.array([100, 50, 75, 30, 200, 120, 150, 20, 80, 110])
# dates = np.array(["2026-07-01", "2026-07-02", "2026-07-03", "2026-07-04", "2026-07-05",
#                   "2026-07-06", "2026-07-07","2026-07-08", "2026-07-09", "2026-07-10"])
#
# total_sales = prices * quantities
# print(f"Общий объем продаж: {total_sales}")
#
# total_sum = np.sum(total_sales)
# print(f"Сумма выручки: {total_sum}")
#
# average_check = np.mean(total_sales)                 #Средний чек по всем продажам
# print(f"Средний чек: {average_check}")
#
# best_product_index = np.argmax(total_sales)
# worst_product_index = np.argmin(total_sales)
# print(f"Лучший товар (ID: {product_ids[best_product_index]}, объем продаж {total_sales[best_product_index]})")
# print(f"Худший товар (ID: {product_ids[worst_product_index]}, объем продаж {total_sales[worst_product_index]})")
# =======================================================================================









# Библиотека Pandas
#
# import pandas as pd

# series1 = pd.Series([10,20,30,40,50])
# print(series1)
#
# series2 = pd.Series({"b": 10, "a": 30, "c": 20})
# print(series2)
#
# # series3 = pd.Series(15)
# series3 = pd.Series(10, index=[3,8,4])
# print(series3)

# age = [36, 16, 23]
# names = ["Сергей", "Роман", "Вадим"]
# series4 = pd.Series(age, index=names, name="age")
# print(series4)
# # print(series4[["Роман", "Вадим"]])
# print("Размер серии:", len(series4))     # кол-во элементов по паитону
# print("Размер серии:", series4.size)    # кол-во элементов по Pandas

# =====================================================

# series = pd.Series([5, 3, 5, 4, 2, 3, 2])
#
# unique_value = series.unique()
# print("Уникальное значение:", unique_value)
#
# value_counts = series.value_counts()
# print("Количество значений в серии\n")
# print(value_counts)

# ===================================================

# age = [36, 16, 23, 29]
# names = ["Сергей", "Роман", "Вадим", "Виталий"]
# series = pd.Series(age, index=names)
# print(series)
#
# elem = series.iloc[[2]]
# print("\nОдин элемент по позиции:", elem)
#
# subset = series.iloc[[0, 2]]
# print("\nНесколько элементов по позиции:")
# print(subset)

# ==========================================================


# series = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# print(series)
#
# print("первые пять элементов:")
# print(series.head())
#
# print("первые три элемента:")
# print(series.head(3))

# print("\nПоследние 5 элементов:")
# print(series.tail())
#
# print("\nПоследние 3 элемента:")
# print(series.tail(3))

# sample_data = series.sample(3)   # выведет 3 случайных значения
# print(sample_data)
# =============================================

# заданное кол-во элементов по какому-то определнному значению
# grades = pd.Series([90, 85, 85, 85, 70], index=["Анна","Борис", "Влад", "Дарья", "Елена"])
# print(grades)
#
# MAX балл
# print(grades.nlargest(2, keep="first"))       # 2 лучших студента которые получили высокий балл
# print(grades.nlargest(2, keep="last"))        # 2 успешных студентов
# print(grades.nlargest(2, keep="all"))
# указываем  keep="first", "last", "all" когда есть одинаковые значения
#
# MIN баллы
# print(grades.nsmallest(3, keep="first"))
# print(grades.nsmallest(3, keep="last"))
# print(grades.nsmallest(3, keep="all"))


#====================================================

# import pandas as pd
#

# s1 = pd.Series([1, 2, 3, 4, 5])
# s2 = pd.Series([6, 7, 8, 9, 10])
#
# # s3 = s1 + s2
# # s3 = s2 - s1
# # s3 = s1 * s2
# s3 = s2 / s1
# print(s3)
#=============================

# s1 = pd.Series(["a", "b", "c", "w", "r"])
# s2 = pd.Series(["d", "e", "f"])
#
# s3 = s1 + s2
# print(s3)

#==========================

# s1 = pd.Series([1, 2, 3, 4, 5])
# s2 = s1 + 5
# print(s2)

#================================
# Фильтры данных в Pandas
# s = pd.Series ([10, 20, 30, 40, 50])
#
# filtered_data = s[s >= 30]
# print(filtered_data)

# s = pd.Series(["Сергей", "Роман", "Вадим", "Виталий", "Сергей", "Вадим"])
# filtered_data = s[s == "Сергей"]
# print(filtered_data)


# s = pd.Series([1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
#
# # filtered_data = s[(s > 8) & (s < 30)]
# filtered_data = s[(s > 8) | (s < 30)]     # False | True
# print(filtered_data)


# s = pd.Series(["Сергей", "Роман", "Вадим", "Виталий", "Адександр", "Артем"])        # isin
# filtered_data = s[s.isin(["Роман", "Игорь", "Артем"])]
# print(filtered_data)


# s = pd.Series([1, 2, 3, 5, 8, 13, 21, 34, 55, 89])                                 # between
# filtered_data = s[s.between(8, 30)]
# print(filtered_data)

#===========================================

# s = pd.Series(['1.0', '2', 'ошибка', '4.5'])
#
# # res = pd.to_numeric(s, errors='coerce')
# res = s.astype(int, errors='ignore')
# print(res)


#==========================================

# DataFrame

# data = {
#     "Name": ["Сергей", "Анна", "Роман", "Александр"],
#     "Age": [28, 36, 23, 42],
#     "City": ["Сочи", "Москва", "Воронеж", "Армавир"]
# }

# df = pd.DataFrame(data)
# print(df)
# print("*" * 30)
# cities = df["City"]        # получение данных  в стобце "City"
# print(cities)
# print("*" * 30)
# cities = df.City           # тоже самое как и предыдущее
# print(cities)
# print("*" * 30)
# columns = ["City", "Name"]      # название столбцов будет сверху
# print(df[columns])
# # print(df[["City", "Name"]])
# print("*" * 30)
# int_columns = df.select_dtypes(include="int64")
# print(int_columns)


# df = pd.DataFrame(data, index=['str_1', 'str_2', 'str_3', 'str_4'])
# print(df)
# print("*" * 30)
# # print(df.loc['str_2'])                      # выведет 1 строку
# # print(df.loc['str_1':'str_3'])                # строки покажет с 1 по 3, вкл последнее значение
# # print(df.loc[['str_1','str_3']])
# print(df.iloc[0])
# print("*" * 30)
# print(df.iloc[1:3])                             # не вкл 3 элемент

# print(df["City"]["str_3"])
# print("*" * 30)
# print(df["City"][1:3])
# print("*" * 30)
# print(df["City"]["str_2": "str_4"])              # вкл 4 элемент
# print("*" * 30)
# print(df["City"][["str_1", "str_3", "str_4"]])

#=============
# 1 вариант
# column = ["City", "Name"]
# print(df[column][1:3])

# 2 вариант такой же, но короче
# print(df[["City", "Name"]][1:3])
#=================================

# print(df.shape)                       # показывает количество строк и кол-во столбцов
# print(df.dtypes)                      # показывает типы данных каждого столбца





# =========================
#
# rows = [
#     ["ноутбук", 50000, 5],
#     ["Смарфон", 30000, 10],
#     ["Наушники", 5000, 5]
# ]
#
# df_product = pd.DataFrame(rows, columns=['Товар', 'Цена', 'Количество'])
# print(df_product)
#
# print("*" * 50)
#
# api_data = [
#     {"ФИО": "Иванов И.И.", "Департамент": "IT"},
#     {"ФИО": "Петров П.П.", "Департамент": "HR"},
#     {"ФИО": "Сидоров С.С."}
# ]
#
# df = pd.DataFrame(api_data)
# print(df)


#=========================================================

# import numpy as np
# import pandas as pd

# data = np.array([
#     ["Tom", 41, "Yandex"],
#     ["Bob", 56, "VK"],
#     ["Sam", 31, "Sberbank"]
# ])
#
# columns = ["Name", "Age", "Company"]
# df = pd.DataFrame(data, columns=columns)
# print(df)

# data = pd.read_excel("data.xlsx")              # excel
# print(data)
# print("*" * 50)
# # print(data.head(3))
# # print(data.tail(3))
# print(data.Age.describe())
# print("*" * 50)
# print(data.describe())

# df = pd.read_json("people.json")              # json
# print(df)

# df = pd.read_csv("internet.csv")                # csv
# print(df)
# print("*" * 50)
# print(df.sort_values("mobile", ascending=False))
# print(df.dropna())



# Занятие 12
# new_country = {"country": "Галактика", "broadband": 1234, "mobile": 295.45}
# df1 = pd.DataFrame([new_country])
# print(df1)
# print("*" * 50)
# new_list1 = pd.concat([df1, df], ignore_index=True)   # добавление строки
# print(new_list1)
# new_list1.to_csv("new_country.csv", index = False)           # переименовать файл
# new_list1.to_csv("new_data.txt", index = False)             # И сохранение файла
# new_list1.to_string("new_data1.txt", index = False)            # 2 способ сохранение файла
# print("*" * 50)
# new_list1.drop(0, inplace=True)                             # удаление строки
# print(new_list1)



# df = pd.read_csv("internet.csv")                # csv
# print(df)
# print("*" * 50)
# print(df[df['mobile'] > 100])
# filtered_data = df[df['country'].str.startswith("S")]       # фильтация столбцов по какому то значению
# print(filtered_data)
# print(df['broadband'].agg(['mean']))                          # agg
# print("*" * 50)
# print(df['broadband'].agg(['min', 'max', 'median']))          # agg

#==================================

# df = pd.read_csv("internet.csv")                               # csv
# print(df)
# print("*" * 50)
# for row_label, row in df.items():
#     print(row_label, row, sep="\n", end="\n\n")              # выводит каждый столбец отдельно
# print("*" * 50)
# for row_label, row in df. iterrows():                       # получаем данные по строкам
#     print(row_label, row, sep="\n", end="\n\n")
# for item in df.itertuples():                                # получить именнованные кортежи
#     print(item, sep="\n", end="\n\n")

#====================================================================
#
# data = {
#     "User_ID": [101, 102, 101, 103, 101],
#     'City': ['Москва', 'Питер', 'Москва', 'Казань', 'Сочи'],
#     'Spend': [500, 700, 500, 300, 1200]
# }
#
# df = pd.DataFrame(data)
# print(df)
# print("*" * 30)
# duplicates = df.duplicated()                             # для нахождения дубликатов
# print(duplicates)
# print("*" * 30)
# df_cleaned = df.drop_duplicates().reset_index(drop = True)   # удаление повторяющихся строк
# print(df_cleaned)

# df_cleaned = df.drop_duplicates(subset='User_ID', keep=False)   # нахождение уникальн пользователей и возможно удаление
# print(df_cleaned)
# print("*" * 30)
#
# df. drop_duplicates(inplace=True)  # удаление дубликата с повторяющейся строкой, и изменение в исходном DataFrame
# print(df)

#========================================

# data = {
#     "User_ID": [101, 102, 101, 103, 101],
#     'City': ['Москва', 'Питер', 'Москва', 'Казань', 'Сочи'],
#     'Spend': [500, 700, 500, 300, 1200]
# }
#
# df = pd.DataFrame(data)
# print(df)
# print("*" * 30)

# year = [1147, 1703, 1723, 1893, 1589]                    # добавление столбца
# df["Year"] = year
# print(df)

# new_columns = pd.DataFrame({                                        # добавление нескольких столбцов
#     "Year": [1147, 1703, 1723, 1893, 1589],
#     "Time zone": ["GMT+3", "GMT+3", "GMT+3", "GMT+3", "GMT+3"],
# })

# df = pd. concat([df, new_columns], axis=1)                 # добавление нескольких столбцов продолжение
# print(df)
# print("*" * 30)
# df.drop("Year", axis=1, inplace=True)                      # удаление столбца
# print(df)

# new_row = pd.Series([104, "Воронеж", 1042], index=df.columns)   # добавление строки
# df.loc[len(df)] = new_row
# print(df)
# print("*" * 30)
# new_row = pd.DataFrame([[104, "Воронеж", 1042], [105, "Саратов", 542]], columns=df.columns)      # добавление нескол строк
# df = pd.concat([df, new_row], ignore_index=True)
# print(df)

# df.drop(index=2, inplace=True)                               # удаление строки index = 2
# print("*" * 30)
# rows = [1, 3]
# df.drop(index=rows, inplace=True)                               # удаление нескольких строк index = 1, 3
# print("*" * 30)
# print(df)

#=====================
# В Pandas есть методы описательной статистики (на основе Numpy):

# data = {"Age": [34, 37, 13, 64, 37, 47, 24, 38, 26, 41, 19, 51, 44]}
# df = pd.DataFrame(data)
# print(df)
# print("*" * 30)
# print("Среднее значение:", df["Age"].mean())
# print("*" * 30)
# print("Медиана:", df["Age"].median())
# print("*" * 30)
# print("Мода:", df["Age"].mode()[0])
# print("*" * 30)
# print("Расброс:", df["Age"].var(), "и стандартное отклонение:", df["Age"].std())
# print("*" * 30)
# print("Квантили возраста:")
# print(df["Age"].quantile([0.25, 0.5, 0.75]))
# print("*" * 30)
# print("90-й процентиль возраста:", df["Age"].quantile(0.90))
# print("*" * 30)

#=================

import numpy as np
import pandas as pd
#
# data = {
#     "A": [1, 2, np.nan, 4, None],
#     "B": [None, 6, 7, 8, np.nan]
# }
#
# df = pd.DataFrame(data)
# print("DataFrame до заполнения пропущенных значений:")
# print(df)
# print("*" * 20)
# missing_data = df.isna()
# print(missing_data)
# non_missing_data = df.notna()
# print(non_missing_data)
# print("DataFrame после заполнения пропущенных значений:")
# filled_df = df.fillna(0)
# print(filled_df)
# filled_df = df.copy()
# filled_df["A"] = df["A"].fillna(df["A"].mean())     # здесь создаем копию и вызываем mean
# print(filled_df)
# filled_df = df.copy()
# filled_df["B"] = df["B"].fillna(df["B"].median())     # здесь создаем копию и вызываем медиана
# print(filled_df)

#=======================================
#
# data = {
#     "City": ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань", "Красноярск", "Волгоград"],
#     "Population": [13274, None, 1637, None, 1330, 1212, None],
#     "Time zone": ["GMT+3", "GMT+3", "GMT+7", "GMT+5", "GMT+3", None, "GMT+3"]
# }
#
# df = pd.DataFrame(data)
# print("DataFrame до заполнения пропущенных значений:")
# print(df)
# print("*" * 50)
# not_missing_mask = df.notna()
# non_missing_df = df[not_missing_mask.all(axis=1)]       # показывает строки со значениями
# print(non_missing_df)
# print("*" * 50)
# missing_data = df["Population"].isna()
# print(missing_data)
# print("*" * 50)
# missing_data = df[df["Population"].isna()]    # возвращаются те записи где значение будет отсутствовать в 1 столбце
# print(missing_data)
# print("*" * 50)
# missing_mask = df.isna()                          # выводим для начала все пропущенные значения
# missing_data = df[missing_mask.any(axis=1)]       # определяем строки в которых отсутствует значение в любом из столбцов, получим таблицу с отсутст значениями
# print(missing_data)

# tz_mode = df["Time zone"].mode()[0]
# print("Мода для столбца Time zone", tz_mode)
# print("*" * 50)
# print("DataFrame после заполнения пропущенных значений:")
# df["Time zone"] = df["Time zone"].fillna(tz_mode)
# print(df)
# print("*" * 50)

#============

# data = {
#     'Имя': ['Анна', 'Борис', 'Влад', 'Ольга', 'Марина', 'Роман', 'Екатерина', 'Виктор', 'Ирина'],
#     'Возраст': [25, 34, 41, 28, 19, 20, 36, 41, 38],
#     'Город': ['Москва', 'Санкт-Петербург', 'Казань', 'Сочи', 'Санкт-Петербург', 'Москва', 'Санкт-Петербург', 'Казань', 'Сочи']
# }
#
# df = pd.DataFrame(data)
# print(df)
# print("*" * 50)
# # print(df.groupby("Город")["Возраст"].sum())
# print(df.groupby("Город")["Возраст"].median())


#=========================

# data = {
#     "product_id": [105, 11, 102, 108, 123, 105],
#     "category": [
#         " Электроника ",
#         "Одежда",
#         " Электроника",
#         "Обувь",
#         "Одежда ",
#         " Электроника"
#     ],
#     'price': ["15 000,50", "2 500,00", "Не указана", "1 200", None, "15 000,50"],
#     'quantity': [2, np.nan, 1, 5, 10, 2]
# }
# df = pd.DataFrame(data)
# print(df)
# print("*" * 50)
# df["category"] = df["category"].str.strip()           # удаляет пробелы слева и справа
# # print(df)
# print("*" * 50)
# df["price"] = df["price"].str.replace(" ", "")
# # print(df)
# df["price"] = df["price"].str.replace(",", ".")
# print(df)






#=======================

# ДЗ

# data = {
#     'Имя': ['Анна', 'Борис', 'Влад', 'Ольга'],
#     'Возраст': [25, 34, 41, 28],
#     'Город': ['Москва', 'Санкт-Петербург', 'Казань', 'Сочи']
# }
# df = pd.DataFrame(data)
# print(df)
# print("*" * 50)
# print(df[df['Возраст'] > 30])


#
# data = {
#     'Имя': ['Анна', 'Борис', 'Влад', 'Ольга', 'Марина', 'Роман', 'Екатерина', 'Виктор', 'Ирина'],
#     'Возраст': [25, 34, 41, 28, 19, 20, 36, 41, 38],
#     'Город': ['Москва', 'Санкт-Петербург', 'Казань', 'Сочи', 'Санкт-Петербург', 'Москва', 'Санкт-Петербург', 'Казань', 'Сочи']
# }
# df = pd.DataFrame(data)
# df["Статус"] = np.where(df["Возраст"] >= 30, "Взрослый", "Молодой")
# print(df)


# data = {
#     'Имя товара': ['Монитор', np.nan, 'Мышка', 'Клавиатура'],
#     'Продажи': [15000, 23000, np.nan, 8000]
# }
# df = pd.DataFrame(data)
# print(df)
# print("*" * 50)
# df = df.dropna(subset=["Имя товара"])
# mean_sales = df["Продажи"].mean()
# df["Продажи"] = df["Продажи"].fillna(mean_sales)
# print(df)
