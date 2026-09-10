crows = int(input("Введите количество ворон (цифрой):"))
if 0 <= crows <= 9:
    if crows == 1:
        word = "ворона"
    elif 2 <= crows <= 4:
        word = "вороны"
    else:
        word = "ворон"
    print("На ветке", crows, word)
else:
    print("Ошибка: число должно быть от 0 до 9!")