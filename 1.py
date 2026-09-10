num = 97531
original_num = num
res5 = num % 10
num = num // 10
res4 = num % 10
num = num // 10
res3 = num % 10
num = num // 10
res2 = num % 10
num = num // 10
res1 = num
print("Исходное число:", original_num)
product = res1 * res2 * res3 * res4 * res5
print("Произведение цифр числа", original_num, ":", product)
average = (res1 + res2 + res3 + res4 + res5) / 5
print("Среднее арифметическое:", average)




