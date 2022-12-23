# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]


def minus_list(list):
    len_list = len(list)
    for i in range(0, len_list):
        count = 0
        while count < len_list:
            summ = list[i]
            if summ > list[i]:
                summ_1 = list[i]
            else:
                summ2 = list[i]
                count += 1
                summ3 = summ_1 - summ2
            return summ3


minus_index = minus_list(my_list)
print(minus_index)
