
from mysql.connector import connect
import json

def create_database():
    #Define os parâmetros para acessar o banco de dados local
    with open('params.json', 'r') as params_file:
        db_user_data = json.load(params_file)

    #Primeira conexão com o MySQL
    db_conn = connect(
        user=db_user_data['user'],
        password=db_user_data['password'],
        host='localhost'
    )
    db_cursor = db_conn.cursor()

    db_cursor.execute(
        """CREATE DATABASE IF NOT EXISTS baldussi_db"""
    )