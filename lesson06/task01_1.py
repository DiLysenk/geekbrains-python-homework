"""
Создать класс ​TrafficLight (​светофор) и определить у него один атрибут ​color (​цвет) и метод running (​запуск).

Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.

Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) ​— 2 секунды,
третьего (зеленый) — на ваше усмотрение.

Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.w
"""
import time


class TrafficLight:
    __color: str = None
    __timing: dict
    __next_idx: int = 0

    def __init__(self, red_time: int = 7, yellow_time: int = 2, green_time: int = 5):
        self.__timing = {
            "red": red_time,
            "yellow": yellow_time,
            "green": green_time
        }

    def running(self, color: str):
        if list(self.__timing.keys()).index(color) != self.__next_idx:
            print("Неправильный порядок сигналов")
            exit()

        self.__color = color
        timer = self.__timing[color]

        for second in range(timer):
            print(f"{self} [{second + 1}]")
            time.sleep(1)

        next_idx = self.__next_idx + 1
        self.__next_idx = next_idx if next_idx < len(self.__timing) else 0

    def __repr__(self):
        return f"Текущий режим = {self.__color}"


try:
    traffic_light = TrafficLight(3, 2, 3)
    traffic_light.running("red")
    traffic_light.running("yellow")
    traffic_light.running("green")
    traffic_light.running("red")
except KeyboardInterrupt:
    print("Exit the program")
