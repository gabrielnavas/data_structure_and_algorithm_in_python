num = 22.01
print(f'{num:.2f}') # 22.01

num = 22
print(f'{num}') # 22

num = 1
print(f'{num:0>5}') # 00001
print(f'{num:0<5}') # 10000
print(f'{num:0^5}') # 00100

name = 'gabriel'
unique_char = '#'
print(f'{name:{unique_char}^50}') ######################gabriel######################
print(name.center(50, '#')) ######################gabriel######################

print(name.lower()) # gabriel
print(name.upper()) # GABRIEL
print(name.title()) # Gabriel