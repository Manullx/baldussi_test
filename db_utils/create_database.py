
import mysql.connector
from mysql.connector import connect
import json


def create_database(system_params: dict):

    def first_try() -> None:

        try:
            # Primeira conexão com o MySQL
            conn = connect(
                user=system_params['user'],
                password=system_params['password'],
                host='localhost'
            )
            cursor = conn.cursor()

            # Cria o database mysql caso ele não exista
            cursor.execute(
                """CREATE DATABASE IF NOT EXISTS baldussi_db"""
            )

            #Encerra a conexão com o banco de dados
            cursor.close()
            conn.close()

            # Reescreve o arquivo de parâmetros setados
            with open('params.json', 'w') as params_file:
                system_params['database_already_exists'] = True
                json.dump(system_params, params_file)
                params_file.close()

            print('Database criado com sucesso!')

        except mysql.connector.Error as err:
            raise Exception(f'Erro encontrado durante criação do database: {err}')

    def create_tables(cursor) -> None:

        #Criando tabela com informações do usuário
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users_info (
            user_id INT NOT NULL AUTO_INCREMENT,
            user_first_name VARCHAR(255) NOT NULL,
            user_last_name VARCHAR(255) NOT NULL,
            user_gender VARCHAR(255) NOT NULL,
            user_email VARCHAR(255) NOT NULL,
            user_phone VARCHAR(255) NOT NULL,
            user_cell VARCHAR(255) NOT NULL,
            PRIMARY KEY (user_id)
            )"""
        )

        #Criando tabela com imformações de login do usuário
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users_login (
            user_id INT,
            user_uuid VARCHAR(255) NOT NULL,
            user_username VARCHAR(255) NOT NULL,
            user_password VARCHAR(255) NOT NULL,
            user_salt VARCHAR(255) NOT NULL,
            user_md5 VARCHAR(255) NOT NULL,
            user_sha1 VARCHAR(255) NOT NULL,
            user_sha256 VARCHAR(255) NOT NULL,
            CONSTRAINT user_login_id FOREIGN KEY (user_id) REFERENCES users_info(user_id)
            )"""
        )

        #Criando tabelas com informações de endereço do usuário
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users_addresses (
            user_id INT,
            user_street_name VARCHAR(255) NOT NULL,
            user_street_number INT NOT NULL,
            user_city VARCHAR(255) NOT NULL,
            user_state VARCHAR(255) NOT NULL,
            user_country VARCHAR(255) NOT NULL,
            user_postcode VARCHAR(255) NOT NULL,
            user_latitude VARCHAR(255) NOT NULL,
            user_longitude VARCHAR(255) NOT NULL,
            CONSTRAINT user_location_id FOREIGN KEY (user_id) REFERENCES users_info(user_id)
            )"""
        )

        # Reescreve o arquivo de parâmetros setados
        with open('params.json', 'w') as params_file:
            system_params['tables_already_exists'] = True
            json.dump(system_params, params_file)
            params_file.close()

        print("Tabelas criadas com sucesos!")

    if not system_params['database_already_exists']:
        first_try()

    try:
        # realiza a conexão novamente com o banco de dados, mas com o database incluído na conexão
        db_conn = connect(
            user=system_params['user'],
            password=system_params['password'],
            host='localhost',
            database='baldussi_db'
        )

        db_cursor = db_conn.cursor()

        if not system_params['tables_already_exists']:
            create_tables(
                cursor=db_cursor
            )

        return db_conn, db_cursor

    except mysql.connector.Error as err:
        raise Exception(f'Erro encontrado durante tentativa de conexão com o database: {err}')



