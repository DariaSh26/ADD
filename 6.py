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





#матрицы

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(matrix)
# print(len(matrix))
# print(matrix[1][2])


#=====================================

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




#6 урок




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




#9 урок


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



#распаковка словаря

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











#База данных


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


