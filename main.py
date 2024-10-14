
#Biblioteca os para comandos no cmd e biblioteca json pra converter dict para json e vice-versa
import os
import json

#Verificar se arquivo com parâmetros do usuário existe, caso contrário ele é criado
if 'params.json' not in os.listdir():
    params = {
        'user': str(input('Insira o username: ')),
        'password': str(input('Insira a senha: ')),
        'database_already_exists': False,
        'tables_already_exists': False,
        'users_already_insert': False
    }

    with open('params.json', 'w') as params_file:
        json.dump(params, params_file)
        params_file.close()
else:
    with open('params.json', 'r') as params_file:
        params = json.load(params_file)
        params_file.close()

from db_utils.create_database import *
from db_utils.insert_into_db import *

#Função responsável pela criação do database e tabelas do banco de dados. Retorna conexão efetivada
conn, cursor = create_database(system_params=params)

#Função responsável pela requisição a API randomuser e inserção no bancco de dados
insert_into_db(
    system_params=params,
    db_conn=conn,
    db_cursor=cursor
)


