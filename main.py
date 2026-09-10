# print("Hello Python")
# print("Привет мир")

# name = "admin "
# print("Hello,",name, type(name), id(name))
# age = 20.2
# print (age, type(age), id(age))

# a = b = c = 1
# print(a, b, c)
# print(id(a), id(b), id(c))

# a, b, c = 5, "Hello", 9.2
# print (a, b, c)

# first_name = "admin"
# print(first_name)
#
# firstName = "admin"
# print(firstName)

# import keyword
# print(keyword.kwlist)

# a = 1
# b = 5
# print("a:", a)
# print("b:", b)
# # c = a
# # a = b
# # b = c
#
# a, b = b, a
# print("a:", a)
# print("b:", b)

# print("Hello \
# Python")
# print('Hello \nPython')

# print("\tДокумент \"script.ру\" находится по заданному пути D:\\folder\\file\\script.py")

# s1 = "Hello"
# s2 = "World"
# s3 = s1+ ", " + s2 + "!\t\t"
# print(s3*5)



#
# day = int(input("Ваедите день недели (цифровой): "))
# if  1 <= day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#             print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("выходной день -", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#             print("воскресенье")
# else:
#     print("Такого дня недели не существует")




# month = int(input("Введите порядковый номер месяца (цифрой):"))
# if 1 <= month <= 12:
#      if month == 1 or month == 2 or month == 12:
#          print("Зима")
#      if 3 <= month <= 5:
#          print("Весна")
#      if 6 <= month <= 9:
#          print("Лето")
#      if 10 <= month <= 11:
#          print("Осень")
# elif month >= 12:
#          print("Ошибкка ввода данных")

# num = 97531
# print("Исходное число:", num)
# one = num % 10
# num = num //10
# two = num % 10
# num = num //10
# three = num % 10
# num = num //10
# four = num % 10
# print(one, two, three, four)
# res = one * 1000 + two *100 + three * 10 + four
# print("Обратное число:", res)



#
# a, b = 30, 20
# print (a if a < b else b)
#
# a, b = 30, 40
# print ("a == b" if a == b else "a > b" if a>b else " a < b" )


# n = input("ВВедите первое число:")
# m = input("ВВедите второе число:")
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


n = int(input("Введите целое число: "))
while type(n) ! = int:
    try:

if n % 2 == 0:
    print("Четное")
else:
    print("Нечетное")