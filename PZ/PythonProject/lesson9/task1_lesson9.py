from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.__color = [('Красный', 7), ('Жёлтый', 2), ('Зелёный', 5)]

    def running(self):
        for color in cycle(self.__color):
            print(color[0])
            if color == 'Красный':
                sleep(color[1])
            elif color == 'Жёлтый':
                sleep(color[1])
            else:
                sleep(color[1])


traffic_light = TrafficLight()
traffic_light.running()
