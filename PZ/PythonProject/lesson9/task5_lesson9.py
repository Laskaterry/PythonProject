class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисует ручка')


class Pencil(Stationery):
    def draw(self):
        print('Рисует карандаш')


class Handle(Stationery):
    def draw(self):
        print('Рисует маркер')


stationery = Stationery('канцелярия')
stationery.draw()
pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()
