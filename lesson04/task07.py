"""
Реализовать генератор с помощью функции с ключевым словом ​yield,​ создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: f​or el in fact(n).​

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def fact(number: int):
    temp_result = 1

    if number <= 0:
        yield temp_result

    for x in range(1, number + 1):
        temp_result *= x
        yield temp_result


N = 4

for el in fact(N):
    print(el)
