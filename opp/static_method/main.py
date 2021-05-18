from person import Person

n1 = Person.generate_id()
n2 = Person('Gabriel', 22).generate_id()
print(n1)
print(n2)

