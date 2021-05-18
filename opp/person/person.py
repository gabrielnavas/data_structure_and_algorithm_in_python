from datetime import datetime

class Food:
    def __init__(self, name):
        self.name = name

class Eat:
    def __init__(self, food=None):
        self.eating = False
        self.food=food

    def to_eat(self, who_eat):
        if not self.eating:
            self.eating = True
            print(f'{who_eat}: starting eat {self.food.name}.')        
            return
    
    def stop_eat(self, who_eat):
        if self.eating:
            print(f'{who_eat}: stopping eat.')        
            self.eating = False
            return

class Talk:
    def __init__(self):
        self.talking = False
        self.subject = ''  

    def to_talk(self, subject):
        if not self.talking:
            self.talking = True
            print(subject)

    def stop_talk(self, who_name):
        if self.talking:
            self.talking = False
            print(f'{who_name}: stopped talking.')

class Person:
    year_now = int(datetime.strftime(datetime.utcnow(), '%Y'))

    def __init__(self, name, born: datetime, eat: Eat, talk: Talk):
        self.name = name
        self.born = born
        self.eat = eat
        self.talk = talk

    def to_talk(self, subject):
        self.talk.to_talk(f'{self.name} say: {subject}')
        self.talk.stop_talk(self.name)
    
    def to_eat(self):
        self.eat.to_eat(self.name)
        self.eat.stop_eat(self.name)

   