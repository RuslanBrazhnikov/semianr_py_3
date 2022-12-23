# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


my_list = [2, 3, 5, 9, 3]


def index(list):
    summ = 0
    len_list = len(my_list)
    for i in range(1, len_list, 2):
        summ += my_list[i]
    return summ


summ_index = index(my_list)
print(f'Сумма элементов c нечетными индексами = {summ_index}')
