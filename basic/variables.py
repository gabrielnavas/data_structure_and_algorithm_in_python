"""
  Iniciar com letra, pode conter números, separar por _, letras minúsculas
"""

name = 'Gabriel'
weight = 75
age = 28
height = 1.85
is_more_eighteen = age > 18

print(name) # Gabriel
print(age) # 28
print(height) # 1.85
print(is_more_eighteen) # True
print(type(name)) # <class 'str'>

index_mass_body = weight / (height**2)
round_imc = round(index_mass_body, 2)
print(f'{name} has: {round_imc} IMC.')