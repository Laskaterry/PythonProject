class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']  # разделение подсмотрела в разборе, показалось удобнее
        self._income_bonus = income['bonus']


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return round(self._income_wage + self._income_bonus)


positions = Position('Иван', 'Иванов', 'Джун', {"wage": 13571.90, "bonus": 5000})
print(positions.get_full_name())
print(positions.get_total_income())
