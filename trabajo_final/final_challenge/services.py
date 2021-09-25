import requests

ERROR ='Fallaste terriblemente'

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_username(params={}):
    response = generate_request('https://randomuser.me/api', params)
    if response:
        user = response.get('results')[0]
        return user.get('name').get('first')

    return ''

def get_query_four(params={}):
    """/api/data/getAsistenciaTotalPeliculas"""
    response = generate_request('http://localhost:4000/api/data/getAsistenciaTotalPeliculas',params)
    if response:
        return response
    return ERROR
