"""
    self.data -> public
    self._data -> protected (public _)
    self.__data -> private (_instance._NameClass__attribute)

"""

class Database:
    def __init__(self):
        self._data = {}
        self.__db_type = 'postgres'

class ClientTable(Database):
    table_name = 'client'

    def insert_one(self, name):
        try:
            len_table = len(self._data[self.table_name]) + 1
            new_client = {'id':len_table, 'name':name}
            self._data[self.table_name].append(new_client)
        except:
            new_client = {'id':1, 'name':name}
            self._data[self.table_name] = [new_client]

    def update_one(self, id, name):
        try:
            for client in self._data[self.table_name]:
                if client['id'] == id:
                    client['name'] = name
                    return True
            return False
        except:
            raise f'{id}, {name} not exists'

    def get_one(self, id):
        try:
            for client in self._data[self.table_name]:
                if client['id'] == id:
                    return client
        except:
            return None
        return None
    
    def delete_one(self, id):
        try:
            for client in self._data[self.table_name]:
                if client['id'] == id:
                    self._data[self.table_name].remove(client)
                    return True
        except:
            raise f'{id} not exists'
        return False

    def get_all(self, id=None, name=None):
        try:
            if id and name:
                return [
                    client for client in self._data[self.table_name]
                        if client['id'] == id and client['name'] == name
                ]
            if id and not name:
                return [
                    client for client in self._data[self.table_name]
                        if client['id'] == id 
                ]
            return [
                client for client in self._data[self.table_name]
                    if client['name'] == name 
            ]
        except:
            raise f'{id} not exists'
        return []
