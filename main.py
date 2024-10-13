
#Biblioteca os para comandos no cmd e biblioteca json pra converter dict para json e vice-versa
import os
import json

#Verificar se arquivo com parâmetros do usuário existe, caso contrário ele é criado
if 'params.json' not in os.listdir():
    db_user_data = {
        'user': str(input('Insira o username: ')),
        'password': str(input('Insira a senha: ')),
        'database_already_exists': False,
        'tables_already_exists': False
    }

    with open('params.json', 'w') as params_file:
        json.dump(db_user_data, params_file)

from db_utils.create_database import create_database

#Função responsável pela criação do database e tabelas do banco de dados. Retorna conexão efetivada
db_conn, db_cursor = create_database()

