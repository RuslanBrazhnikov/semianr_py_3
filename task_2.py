# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]

mult_list = []


def mult_num(list):
    len_list = len(my_list)
    i = 0
    count = 0

    while count < (len_list / 2):
        multi_i = list[i] * list[len_list - i - 1]
        mult_list.append(multi_i)
        count += 1
        i += 1
    return mult_list


mult_numbers = mult_num(my_list)
print(f'Произведение пар чисел = {mult_numbers}')
