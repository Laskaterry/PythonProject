class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} едет')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print('Скорость:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышаем!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышаем!')


class PoliceCar(Car):
    pass


sport_car = SportCar(250, 'Красная', 'Спортивная машина')
town_car = TownCar(90, 'Зелёная', 'Городская машина')
work_car = WorkCar(90, 'Жёлтая', 'Рабочая машина')
police_car = PoliceCar(150, 'Синяя', 'Полицейская машина', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.go()
town_car.stop()
work_car.turn('направо')
