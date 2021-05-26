from funcs import get_my_address, get_my_physical_data

street, number = get_my_address()
print(street, number)

height, more_data = get_my_physical_data()
print(height, more_data['weight_kg'])