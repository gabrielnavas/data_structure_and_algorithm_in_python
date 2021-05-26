from funcs import get_f_multiplication

f = get_f_multiplication()
result = f(10)
print(result) # 20

print(type(f)) # <class 'function'>
print(id(f)) # 139740606979520
print(id(get_f_multiplication())) #  139740606979520
print(id(f) == id(get_f_multiplication())) # memory address is True