
import json

#Define os parâmetros para
with open('params.json', 'r') as params_file:
    db_user_data = json.load(params_file)
    params_file.close()

#Biblioteca para realizar as requisições para a api RandomUser
import requests

request_data = {
    'url': 'https://randomuser.me/api/',
    'dataType': 'json'
}


def insert_into_db(system_params: dict, db_conn, db_cursor):

    def create_user(user_data):

        #Insere o usuário na tabela de informações de usuário
        db_cursor.execute(
            """INSERT INTO users
            (user_first_name, user_last_name, user_age, user_birth_date, user_gender, user_email, user_phone, user_cell)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                user_data['name']['first'],
                user_data['name']['last'],
                user_data['registered']['age'],
                user_data['registered']['date'].replace('T', ' ').replace('Z', ''),
                user_data['gender'],
                user_data['email'],
                user_data['phone'],
                user_data['cell']
            )
        )

        #Resgata o id do usuário inserido
        user_id = db_cursor.lastrowid

        #Insere informações de login do usuário
        db_cursor.execute(
            """INSERT INTO users_login
            (user_login_id, user_uuid, user_username, user_password, user_salt, user_md5, user_sha1, user_sha256)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                user_id,
                user_data['login']['uuid'],
                user_data['login']['username'],
                user_data['login']['password'],
                user_data['login']['salt'],
                user_data['login']['md5'],
                user_data['login']['sha1'],
                user_data['login']['sha256']
            )
        )

        #Insere informações de endereço do usuário
        db_cursor.execute(
            """INSERT INTO users_addresses
            (user_address_id, user_street_name, user_street_number, user_city, user_state,
            user_country, user_postcode, user_latitude, user_longitude)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                user_id,
                user_data['location']['street']['name'],
                user_data['location']['street']['number'],
                user_data['location']['city'],
                user_data['location']['state'],
                user_data['location']['country'],
                user_data['location']['postcode'],
                user_data['location']['coordinates']['latitude'],
                user_data['location']['coordinates']['longitude']
            )
        )

        #Manda as inserçoes setadas no cursor para o banco de dados
        db_conn.commit()

    if not system_params['users_already_insert']:
        for _ in range(100):
            request_result = requests.get(request_data['url'])
            create_user(request_result.json()['results'][0])

        with open('params.json', 'w') as params_file:
            system_params['users_already_insert'] = True
            json.dump(system_params, params_file)
            params_file.close()
