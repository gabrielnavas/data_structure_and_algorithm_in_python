from database import ClientTable

cli_table = ClientTable()
cli_table.insert_one('Gabriel')
cli_table.insert_one('John')
cli_table.insert_one('Anna')
print(cli_table._Database__db_type) # postgres
