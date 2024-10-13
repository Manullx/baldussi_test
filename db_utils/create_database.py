import mysql.connector
from mysql.connector import connect
from mysql.connector import errorcode
import json

#Define os parâmetros para acessar o banco de dados local
with open('params.json', 'r') as params_file:
    db_user_data = json.load(params_file)
    params_file.close()

def create_database():

    def first_try():
        try:
            # Primeira conexão com o MySQL
            db_conn = connect(
                user=db_user_data['user'],
                password=db_user_data['password'],
                host='localhost'
            )
            db_cursor = db_conn.cursor()

            # Cria o database mysql caso ele não exista
            db_cursor.execute(
                """CREATE DATABASE IF NOT EXISTS baldussi_db"""
            )

            db_cursor.close()
            db_conn.close()

            # Reescreve o arquivo de parâmetros setados
            with open('params.json', 'w') as params_file:
                db_user_data['database_already_exists'] = True
                json.dump(db_user_data, params_file)
                params_file.close()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuário ou senha incorretors")
            else:
                print(f'Erro encontrado {err}')

    if not db_user_data['database_already_exists']:
        first_try()
    else:

        try:
            # realiza a conexão novamente com o banco de dados, mas com o database setado
            db_conn = connect(
                user=db_user_data['user'],
                password=db_user_data['password'],
                host='localhost',
                database='baldussi_db'
            )
            db_cursor = db_conn.cursor()



        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuário ou senha incorretors")
            else:
                print(f'Erro encontrado {err}')



