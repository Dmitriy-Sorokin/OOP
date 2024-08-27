import requests
import hashlib
import json


def generate_token_without_tps():
    guid = '229d579a-672e-440a-9d91-740728462ffc'
    id = '38001'
    uid = '160'
    currency = 'USD'
    hash_token = hashlib.md5(('GetToken/'
                              + guid
                              + id
                              + uid
                              + currency
                              + 'OLUFTPWB').encode('utf-8')).hexdigest()
    try:
        headers: dict = {'Content-Type': 'application/json; charset=utf-8'}

        # params = {
        # 	"ClientGuid": guid,
        # 	"gameID": id,
        # 	"userID": int(uid),
        # 	"Currency": currency,
        # 	"lang": "RU",
        # 	"clientType": 0,
        # 	"demoMode": False,
        # 	"extraData": 'false',
        # 	"extraBonus": False,
        # 	"apiVersion": "V2",
        # 	"Hash": hash_token,
        # 	'name': 'test',
        # }
        params = {
            "clientGuid": '229d579a-672e-440a-9d91-740728462ffc',
            "gameId": 38001,
            "userId": "160",
            "currency": "USD",
            "lang": "RU",
            "clientType": 0,
            "demoMode": False,
            "extraData": "false",
            "extraBonus": False,
            "apiVersion": "V2",
            "hash": "232cbf5a69d607a737a52a07afe200f0",
        }
        branch = 'mw-4117'
        response = requests.post('https://mw-4117-partner.k8s.dev.slt.lan/partnersV2/GetToken', json=params,
                                 verify=False).json()
        # response = requests.post("https://MW-4117-partner.perfecttlos.com/partnersV2/GetToken/", json=params)
        print(f"https://{branch}-partner.perfecttlos.com/partnersV2/GetToken/")
        print(params)
        print(response)
    # token = response['IframeUrl'].split('token=')[1].split('&')[0]

    except ConnectionError:
        assert False, "Problem with the server."


# return token


print(generate_token_without_tps())
