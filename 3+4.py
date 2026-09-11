# res = 1
#
# while True:
#     n = int(input("Введите число:"))
#     if n == 0:
#         break
#     res *= n
#
# print("Результат:, res")


# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1   #таблица умножения пример
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i*j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#           print("+", end="")
#         else:
#           print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#     print(element)

# for i in "Hello!":
#     print(i)

# for i in "red", "orange", "yellow", "green", "blue", "violet":
#     print(i)

# print(range(start, stop, step))    №расшифровка range
# for i in range(2, 9, 3):
#       print(i, end=" ")
#
# print()
#
# j = 2
# while j < 9:
#     print(j, end=" ")
#     j += 3
#
# for i in range(9, 0, -1):
#     print(i, end=" ")
#
#
# print()
# j = 9
# while j > 0:
#     print(j, end=" ")
#     j -= 1

# for i in range(10,100):
#     print(i, end=" ")

# for i in range(10,100):     № целые числа в диапазоне от 10 до 100 у которых есть 2 одинаковые цифры
#     if i % 10 == i // 10:
#        print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('else')

# for i in range(4):              #строка
#     for j in range(12):         #столбец
#         print("*", end="")
#     print()

# for i in range(4):              #строка
#     for j in range(16):
#         if i == 0 or j == 0 or i == 3 or j == 15:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# num = [i * 2 for i in "Hello"]
# print(num)

# num = [i for i in range(10) if i % 2 == 0]
# print(num)


# nums = [8, 3, 9, 4, 1]
# print(nums)

# print(nums[4])
# print(nums[2])
# print(nums[-1])

# nums[-1] = 256
# nums[3] += 100
# print(nums)
#
# print("Длина списка:", len(nums)) №автоматически посчитать длину списка

# s = [1,3,5]
# print(s * 2, type(s))

# b = list("Hello")
# print(b, type(b))

# n = list(range(2, 10, 2))
# n = list(range(10, 2, -2))
# print(n)

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)

# a = [0] * int(input("Введите количество элементов списка: "))    #гаполнить список с клавиатуры
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("->"))
#     print(a)

# a = [input("->") for i in range(int(input("n = ")))]  #более короткая чем до этого. Называется генератор списка
# print(a)

# a = [9, 7, 5, 1, 2]
#
# for i in range (len(a)):        # i = 0 1 2 3 4
#     print(a[i], end=" ")
#
# print()
#
# for el in a:      # el = 9 7 5 1 2
#     print(el, end=" ")




# a = [int(input("->")) for _ in range(int(input("n = ")))]
# print(a)
#
# s = 0
# # for i in range(len(a)):  № 1 способ более длинный
# #     if a[i] < 0:
# #         s += a[i]
# # for i in a:                # 2 короткий способ
# #     if i < 0:
# #         s += 1
# print("Сумма отрицательных элементов:", s)



# a = [int(input("->")) for _ in range(int(input("n = ")))]
# print(a)

# for i in range(1, len(a)):               # правильное рещшение, если нужно сравнить с пред числом
#     if a[i] > a[i-1]:
#     print(a[i], end=" ")





# n = list(range(21, 41))
# print(n)
#
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print("Количество четных элементов списка:", k)
# print("Сумма нечетных элементов:", s)



# a = [7, 9, 2, 1, 3]
# a[0], a[1] = a[1], a[0]
# print(a)






# Срезы
# # список[start:stop:step]
# a = [7, 9, 2, 1, 3, 8]
# # 0, 1, 2, 3, 4, 5
# print(a, len(a))
# print(a[1:4])
# print(a[2:])
# print(a[:2])
# print(a[1::2])
# print(a[5::-1])
# print(a[5::-1])


# a = [7, 9, 2, 1, 3, 8]
# print(a, len(a))
# print(a[1:3])
# а[1:3] = [0, 0, 0, 0]
# print(a, len(a))

#
# print(dir(list))
# a = [7, 9, 2, 1, 3, 8]





# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число:"))
#     # s.append(x)
#     s.insert(num, x)
# print(s)


# a = [1,2,3]
# b = [11,22,33]
# с = []
#
# for i in range (len(a)):
#     c.append(a[i])
#     c.append(b[i])
#
# print(c)

# import random
#
# lst = [random.randint(a:0, b:100) for _ in range(10)]
# print(lst)
# maximum = max(lst)
# print("max =", maximum)
# lst.remove(maximum)
# lst.insert(0, maximum)
# print(lst)

#Матрицы

# matrix = [
#     [1, 2, 3,4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(matrix)
# print(len(matrix))
# print(matrix[0])
# for row in range(len(matrix)):
#     print(matrix[row])
#     for col in range(len(matrix[row])):
#         print(matrix[row][col], end="\t")
#     print()
# #=================
# for row in matrix:
#     for col in row:
#         print(col, end="\t")
#     print()

# import math
#
# print(math.sgrt(4))
# print(math.ceil(3.2))
# print(math.floor(3.8))
# print(math.pi)

# def hello(name):   #аргумент
#     print("Hello,", name)
#
#
# hello("Irina")     #параметы
# hello("Ivan")

# def get_sum(a:{__add__}, b):
#     print(a+b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# n = 3
# m = 6
# get_sum(n, m)

# def cube(a:{__mul__}):
#     return a * a * a
#
# for i in range(1, 11):
#     print(1, "в кубе =", cube(i))

# def change(lst):
#     # last =lst.pop()
#     # first = lst.pop(0)
#     # lst.insert(0,last)
#     # lst.append(first)
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1,2,3]))
# print(change([9, 12, 33,54, 105]))
# print(change(["с", "л","о", "н"]))



