"""
Программа принимает действительное положительное число ​x и целое отрицательное число y.​
Необходимо выполнить возведение числа ​x в степень ​y.
​Задание необходимо реализовать в виде функции ​my_func(x, y).​
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.

Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func(x, y):
    # решение через оператор
    # return x ** y

    # решение через цикл
    powered = x

    if y > 0:
        for _ in range(1, y):
            powered *= x
    else:
        for _ in range(1, y, -1):
            powered /= x

    return powered


a, b = float(input("Число a >>> ")), int(input("Число b >>> "))

print(my_func(a, b))
