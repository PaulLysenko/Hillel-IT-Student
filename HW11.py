class vihicle:
    max_speed = 0
    def __init__(self, maximum_speed):
        self.max_speed = maximum_speed


class car(vihicle):
    def message(self):
        return f'Average maximum car speed is {self.max_speed}'


class plane(vihicle):
    def message(self):
        return f'Average maximum plane speed is {self.max_speed}'


class ship(vihicle):
    def message(self):
        return f'Average maximum ship speed is {self.max_speed}'


car1 = car(100)
print(car1.message())

ship1 = ship(80)
print(ship1.message())

plane1 = plane(900)
print(plane1.message())
