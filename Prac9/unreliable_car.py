from random import randint
from Prac9.car import Car


class Unreliable(Car):
    '''An unreliable make of car'''

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability




