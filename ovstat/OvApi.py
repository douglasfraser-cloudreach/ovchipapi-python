import requests
import sys
import json

CLIENT_ID     = "nmOIiEJO5khvtLBK9xad3UkkS8Ua"
CLIENT_SECRET = "FE8ef6bVBiyN0NeyUJ5VOWdelvQa"
class OvApi:
    def __init__(self,username,password):
        self.id_token = self.get_token(username,password)
        self.authorizationToken = self.get_authorization()
    def get_token(self,username, password, client_id=CLIENT_ID, client_secret=CLIENT_SECRET):
        post_data = {"username": username,
                     "password": password,
                     "client_id": client_id,
                     "client_secret": client_secret,
                     "grant_type": "password",
                     "scope": "openid"}

        r = requests.post("https://login.ov-chipkaart.nl/oauth2/token", data = post_data).json()
        if 'id_token' not in r:
            print(r)
            sys.exit(-1)
        return r["id_token"]

    def refresh_token(self,refresh_token, client_id=CLIENT_ID, client_secret=CLIENT_SECRET):
        post_data = {"refresh_token": refresh_token,
                     "client_id": client_id,
                     "client_secret": client_secret,
                     "grant_type": "refresh_token"}

        return requests.post("https://login.ov-chipkaart.nl/oauth2/token", data = post_data).json()

    def get_authorization(self):
        post_data = {"authenticationToken": self.id_token}

        response = requests.post("https://api2.ov-chipkaart.nl/femobilegateway/v1/api/authorize", data = post_data)
        as_json = response.json()
        return as_json['o']

    def get_cards_list(self, locale="nl-NL"):
        post_data = {"authorizationToken": self.authorizationToken,
                     "locale": locale}

        response = requests.post("https://api2.ov-chipkaart.nl/femobilegateway/v1/cards/list", data = post_data)
        as_json = response.json()
        return as_json['o']

    def get_transaction_list(self, mediumId, offset = 0, locale="nl-NL"):
        transactions = []

        post_data = {"authorizationToken": self.authorizationToken,
                     "mediumId": mediumId,
                     "offset": offset,
                     "locale": locale}

        response = requests.post("https://api2.ov-chipkaart.nl/femobilegateway/v1/transaction/list", data = post_data)
        as_json = response.json()
        transactions += as_json['o']['records']

        while offset < as_json['o']['nextOffset']:
            post_data['offset'] = as_json['o']['nextOffset']
            response = requests.post("https://api2.ov-chipkaart.nl/femobilegateway/v1/transaction/list", data = post_data)
            as_json = response.json()
            transactions += as_json['o']['records']
            offset = int(as_json['o']['nextOffset'])

        return transactions
