""" Services consume a 'api_flask' """
import requests

ERROR = 'Fallaste terriblemente'


def generate_request(url):
    """Requerido para consumir api"""
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return ERROR

#IMPORT DATA
def get_import_data():
    """Importa los datos a la db en mongo"""
    response_import = generate_request(
        'http://localhost:4000/api/data/importcsv'
    )
    if response_import:
        return response_import
    return ERROR

#QUERY ONE
def get_query_one(fecha_inicio, fecha_final, anio):
    """docstring"""
    response_query_one = generate_request(
        f'http://localhost:4000/api/data/getTotalPersonaPais/{fecha_inicio}/{fecha_final}/{anio}'
    )
    if response_query_one:
        return response_query_one
    return ERROR

#QUERY TWO
def get_query_two(fecha_inicio, fecha_final, anio):
    """docstring"""
    response_query_two = generate_request(
        f'http://localhost:4000/api/data/getTotalPersona/{fecha_inicio}/{fecha_final}/{anio}'
    )
    if response_query_two:
        return response_query_two
    return ERROR

#QUERY THREE
def get_query_three(fecha_inicio, fecha_final, anio):
    """docstring"""
    response_query_three = generate_request(
        f'http://localhost:4000/api/data/getTotalPersonasCadenaPais/{fecha_inicio}/{fecha_final}/{anio}'
    )
    if response_query_three:
        return response_query_three
    return ERROR

def get_query_three_pais_cadena(fecha_inicio, fecha_final, anio, pais, cadena):
    """docstring"""
    response_query_three_pais_cadena = generate_request(
        f'http://localhost:4000/api/data/getTotalPersonasCadenaPais_Pais_Cadena/{fecha_inicio}/{fecha_final}/{anio}/{pais}/{cadena}'
    )
    if response_query_three_pais_cadena:
        return response_query_three_pais_cadena
    return ERROR

def get_query_three_pais(fecha_inicio, fecha_final, anio, pais):
    """docstring"""
    response_query_three_pais = generate_request(
        f'http://localhost:4000/api/data/getTotalPersonasCadenaPais_Pais/{fecha_inicio}/{fecha_final}/{anio}/{pais}'
    )
    if response_query_three_pais:
        return response_query_three_pais
    return ERROR

def get_query_three_cadena(fecha_inicio, fecha_final, anio, cadena):
    """docstring"""
    response_query_three_cadena = generate_request(
        f'http://localhost:4000/api/data/getTotalPersonasCadenaPais_Cadena/{fecha_inicio}/{fecha_final}/{anio}/{cadena}'
    )
    if response_query_three_cadena:
        return response_query_three_cadena
    return ERROR
#QUERY FOUR
def get_query_four(pelicula):
    """/api/data/getAsistenciaTotalPeliculas"""
    response_query_four = generate_request(
        f'http://localhost:4000/api/data/getAsistenciaTotalPeliculas/{pelicula}'
    )
    if response_query_four:
        return response_query_four
    return ERROR
#QUERY FIVE
def get_query_five(pelicula):
    """El total de personas que vieron cada pelicula en centroamerica por cadena de cine"""
    response_query_five = generate_request(
        f'http://localhost:4000/api/data/getAsistenciaCadenaPeliculas/{pelicula}')
    if response_query_five:
        return response_query_five
    return ERROR
#QUERY SIX
def get_query_six(pelicula):
    """El total de personas que vieron cada pelicula en centroamerica por cadena de cine"""
    response_query_six = generate_request(
        f'http://localhost:4000/api/data/getAsistenciaCadenaPeliculasPorcentaje/{pelicula}')
    if response_query_six:
        return response_query_six
    return ERROR
#QUERY SEVEN
def get_query_seven(fecha_inicio, fecha_final, anio, pelicula):
    """Mostrar para cada pelicula el total de personas que acudieron a verla en la
    semana por pais y ordenarla de la más vista a la menos vista"""
    response_query_seven = generate_request(
        f'http://localhost:4000/api/data/getMasVistaMenosVista/{fecha_inicio}/{fecha_final}/{anio}/{pelicula}')
    if response_query_seven:
        return response_query_seven
    return ERROR
#QUERY EIGHT
def get_query_eight(fecha_inicio, fecha_final, anio, pais, pelicula):
    """Total de personas por cadena de cine, por pais, por semana"""
    response_query_eight = generate_request(
        f'http://localhost:4000/api/data/getAsistenciaCinePaisFecha/{fecha_inicio}/{fecha_final}/{anio}/{pais}/{pelicula}')
    if response_query_eight:
        return response_query_eight
    return ERROR
#QUERY NINE
def get_query_nine(fecha_inicio, fecha_final, anio, pais, pelicula):
    """Total de personas por cadena de cine, por pais, por semana en porcentaje"""
    response_query_nine = generate_request(
        f'http://localhost:4000/api/data/getAsistenciaCinePaisPorcentaje/{fecha_inicio}/{fecha_final}/{anio}/{pais}/{pelicula}')
    if response_query_nine:
        return response_query_nine
    return ERROR


#AUXILIARES
def get_fecha_pelicula(fecha_inicio, fecha_final, anio):
    """Muestra las peliculas que se mostraron en una semana"""
    response_fecha_pelicula = generate_request(
        f'http://localhost:4000/api/data/getFechaPeliculas/{fecha_inicio}/{fecha_final}/{anio}'
    )
    if response_fecha_pelicula:
        return response_fecha_pelicula
    return ERROR

def get_fecha_pais_pelicula(fecha_inicio, fecha_final, anio, pais):
    """Muestra las peliculas que se mostraron en una semana en determinado pais"""
    response_fecha_pais_pelicula = generate_request(
        f'http://localhost:4000/api/data/getFechaPaisPeliculas/{fecha_inicio}/{fecha_final}/{anio}/{pais}'
    )
    if response_fecha_pais_pelicula:
        return response_fecha_pais_pelicula
    return ERROR