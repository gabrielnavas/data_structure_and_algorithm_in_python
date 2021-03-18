"""
  Iniciar com letra, pode conter números, separar por _, letras minúsculas
"""

nome = 'Gabriel'
peso = 75
idade = 28
altura = 1.85
maior_idade = idade > 18

print(nome) # Gabriel
print(idade) # 28
print(altura) # 1.85
print(maior_idade) # True
print(type(nome)) # <class 'str'>

indice_massa_corporal = peso / (altura**2)
round_imc = round(indice_massa_corporal, 2)
print(f'{nome} tem: {round_imc}')