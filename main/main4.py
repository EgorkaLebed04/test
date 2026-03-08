import requests
from config import TOKEN


headers = {'Authorization': f'OAuth {TOKEN}'}
url_yd = 'https://cloud-api.yandex.net'
name_folder = "pd-fpy_140"

def create_folder():
    params = {'path': 'pd-fpy_140'}
    response = requests.put(url_yd + '/v1/disk/resources', params=params, headers=headers)
    # print(str(response.status_code)[0])
    return response

def get_folder():
    params = {'path': 'pd-fpy_140'}
    response = requests.get(url_yd + '/v1/disk/resources', params=params, headers=headers)
    # print(response.json())
    return response

get_folder()