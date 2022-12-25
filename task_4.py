# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number = int(input('Введите число: '))

new_number = []

while number > 0:
    new_number.append(number % 2)
    number //= 2

print(*new_number, sep='')
