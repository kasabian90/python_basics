# 1) Найти произведение всех четных чисел от 1 до 100.
def even_nums():
    i = 2
    mult = 1
    while i <= 100:
        mult *= i
        i += 2
    print(mult)

# 2) Пользователь вводит два числа (a, b). Найти количество всех нечетных чисел в диапазоне от a до b (a < b).
def odd_nums():
    a = int(input())
    b = int(input())
    c = 0;
    for i in range (a, b + 1):
        if i % 2 != 0:
            c += 1
    print(c)
