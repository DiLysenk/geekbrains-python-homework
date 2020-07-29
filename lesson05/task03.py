"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32
"""

with open("task03.txt") as f:
    worker_list = [worker_line.split() for worker_line in f.readlines()]

workers_with_info = [
    {"name": worker[0], "salary": float(worker[1])}
    for worker in worker_list
    if len(worker) > 1
]

# простой вариант с циклом
for worker in workers_with_info:
    if worker['salary'] < 20_000:
        print(worker['name'])

# вариант с filter
for worker in filter(lambda item: item["salary"] < 20_000, workers_with_info):
    print(worker['name'])
