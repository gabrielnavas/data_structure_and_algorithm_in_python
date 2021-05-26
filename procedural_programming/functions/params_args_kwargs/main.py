from funcs import people, country

people('gabriel', 'john', 'anna') # gabriel john ['anna']

data = country(name='Gabriel', age=25)
print(data['name']) # Gabriel
print(data['age']) # 25