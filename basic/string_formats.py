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
phrase_option1 = f'{name} has:{index_mass_body: .2f} IMC.'
phrase_options2 = '{} has: {:.2f} IMC.'.format(name, index_mass_body)
phrase_option3 = '{0} has: {1:.2f} IMC.'.format(name, index_mass_body)
phrase_option4 = '{n} has: {imc:.2f} IMC.'.format(n=name, imc=index_mass_body)

print(phrase_option1)
print(phrase_options2)
print(phrase_option3)
print(phrase_option4)