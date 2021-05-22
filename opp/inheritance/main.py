from database import ClientTable

db = ClientTable()
db.insert_one('Gabriel')
db.insert_one('John')
db.insert_one('Richard')

print(db.data)

print('Get user id 2')
john = db.get_one(2)
print(f'new user: {john}')

print('update user id 2')
is_update = db.update_one(2, 'Anna')
print(f'isUpdate: {is_update}')

print('delete user id 2')
is_delete = db.delete_one(2)
print(f'isUpdate: { is_delete }')

print('delete user id 2 again')
is_delete = db.delete_one(2)
print(f'isUpdate: { is_delete }')

print('get user 3')
user_3 = db.get_one(3)
print('user 3: {user_3}')

all_users = db.get_all(name='Obama')
print(all_users)

all_users = db.get_all(name='Gabriel')
print(all_users)

all_users = db.get_all(id=1, name='Gabriel')
print(all_users)

all_users = db.get_all(id=1)
print(all_users)

all_users = db.get_all(id=1, name='Gabriel')
print(all_users)

all_users = db.get_all()
print(all_users)