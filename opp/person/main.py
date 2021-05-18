from person import Person, Eat, Food, Talk
from datetime import datetime

food = Food('Banana')
eat = Eat(food=food)
talk = Talk()

p1 = Person('Gabriel', born=datetime(1970, 2, 2, 16,0,0,0), eat=eat, talk=talk)
p2 = Person('Anna', born=datetime(1980, 6, 7, 2,15,0,0), eat=eat, talk=talk)

print(p1 == p2) # False
print(p1) # <person.Person object at 0x7fac43445fa0>
print(p2) # <person.Person object at 0x7fac43445850>

p2.to_talk('Hey, you')
p2.to_eat()
