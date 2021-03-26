name = 'gabriel'

print(name[0]) # 'g'
print(name[-1]) # l
print(name[-2]) # e

print(name[1:]) # 'abriel'
print(name[1:3]) # 'ab'

print(name[::1]) # 'gabriel'
print(name[::2]) # 'gbil'
print(name[::3]) # 'grl'

print(name.replace('a', '@')) # G@briel