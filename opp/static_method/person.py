from random import randint

class Person:
    year_now = 2021

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def generate_id():
        rand = randint(10000, 19999)
        return rand