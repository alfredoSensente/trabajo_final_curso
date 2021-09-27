""" Services consume a 'api_flask' """
import requests

ERROR = 'Fallaste terriblemente'


def generate_request(url):
    """Requerido para consumir api"""
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return ERROR


def get_query_one(fecha_inicio, fecha_final, anio):
    """docstring"""
    response_query_one = generate_request(
        f'http://localhost:4000/api/data/getTotalPersonaPais/{fecha_inicio}/{fecha_final}/{anio}'
    )
    if response_query_one:
        return response_query_one
    return ERROR


def get_query_two(fecha_inicio, fecha_final, anio):
    """docstring"""
    response_query_two = generate_request(
        f'http://localhost:4000/api/data/getTotalPersona/{fecha_inicio}/{fecha_final}/{anio}'
    )
    if response_query_two:
        return response_query_two
    return ERROR


def get_query_three(fecha_inicio, fecha_final, anio):
    """docstring"""
    response_query_three = generate_request(
        f'http://localhost:4000/api/data/getTotalPersonasCadenaPais/{fecha_inicio}/{fecha_final}/{anio}'
    )
    if response_query_three:
        return response_query_three
    return ERROR


def get_query_four():
    """/api/data/getAsistenciaTotalPeliculas"""
    response_query_four = generate_request(
        'http://localhost:4000/api/data/getAsistenciaTotalPeliculas')
    if response_query_four:
        return response_query_four
    return ERROR


def get_query_five():
    """El total de personas que vieron cada pelicula en centroamerica por cadena de cine"""
    response_query_five = generate_request(
        'http://localhost:4000/api/data/getAsistenciaCadenaPeliculas')
    if response_query_five:
        return response_query_five
    return ERROR


def get_query_six():
    """El total de personas que vieron cada pelicula en centroamerica por cadena de cine"""
    response_query_six = generate_request(
        'http://localhost:4000/api/data/getAsistenciaCadenaPeliculasPorcentaje')
    if response_query_six:
        return response_query_six
    return ERROR

def get_query_seven(fecha_inicio, fecha_final, anio):
    """Mostrar para cada pelicula el total de personas que acudieron a verla en la
    semana por pais y ordenarla de la más vista a la menos vista"""
    response_query_seven = generate_request(
        f'http://localhost:4000/api/data/getMasVistaMenosVista/{fecha_inicio}/{fecha_final}/{anio}')
    if response_query_seven:
        return response_query_seven
    return ERROR

def get_query_eight(fecha_inicio, fecha_final, anio, pais):
    """Total de personas por cadena de cine, por pais, por semana"""
    response_query_eight = generate_request(
        f'http://localhost:4000/api/data/getAsistenciaCinePaisFecha/{fecha_inicio}/{fecha_final}/{anio}/{pais}')
    if response_query_eight:
        return response_query_eight
    return ERROR

def get_query_nine(fecha_inicio, fecha_final, anio, pais):
    """Total de personas por cadena de cine, por pais, por semana en porcentaje"""
    response_query_nine = generate_request(
        f'http://localhost:4000/api/data/getAsistenciaCinePaisPorcentaje/{fecha_inicio}/{fecha_final}/{anio}/{pais}')
    if response_query_nine:
        return response_query_nine
    return ERROR
