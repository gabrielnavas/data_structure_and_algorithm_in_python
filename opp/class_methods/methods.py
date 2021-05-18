class Person:
    year_now = 2021

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def to_year_born(cls, name, year_born):
        age = cls.year_now - year_born
        return cls(name, age)
   