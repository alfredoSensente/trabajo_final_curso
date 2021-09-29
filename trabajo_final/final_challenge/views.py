"""Views de final_challenge"""
from django.shortcuts import render
from .services import get_query_one
from .services import get_query_four
from .services import get_query_two
from .services import get_query_three
from .services import get_query_three_pais_cadena
from .services import get_query_three_pais
from .services import get_query_three_cadena
from .services import get_query_five
from .services import get_query_six
from .services import get_query_seven
from .services import get_query_eight
from .services import get_query_nine

from .services import get_fecha_pelicula
from .services import get_fecha_pais_pelicula


# Create your views here.

def query_one(request):
    """Formulario para ingresar los parametros para mostrar template table_one"""
    if request.method == 'POST':
        fecha_inicio = request.POST['inputFechaInicio']
        fecha_final = request.POST['inputFechaFinal']
        context = {
            'query_one': get_query_one(
                fecha_inicio[-5:],
                fecha_final[-5:],
                fecha_final[:4]
            ),
            'fecha_inicio': fecha_inicio,
            'fecha_final': fecha_final,
        }
        return render(request, 'final_challenge/templates/tables/table_one.html', context)
    return render(request, 'final_challenge/templates/tables/table_one.html')


def query_two(request):
    """Mostrar el total de personas de los 5 paises que visitaron el cine en la semana"""
    if request.method == 'POST':
        fecha_inicio = request.POST['inputFechaInicio']
        fecha_final = request.POST['inputFechaFinal']
        context = {
            'query_two': get_query_two(
                fecha_inicio[-5:],
                fecha_final[-5:],
                fecha_final[:4]
            ),
            'fecha_inicio': fecha_inicio,
            'fecha_final': fecha_final,
        }
        return render(request, 'final_challenge/templates/tables/table_two.html', context)
    return render(request, 'final_challenge/templates/tables/table_two.html')


def query_three(request):
    """Mostrar el total de personas de los 5 paises que visitaron el cine en la semana"""
    if request.method == 'POST':
        fecha_inicio = request.POST['inputFechaInicio']
        fecha_final = request.POST['inputFechaFinal']
        if (request.POST.get('inputTextPais', False) and
            request.POST.get('inputTextCadena', False)):
            pais = request.POST['inputTextPais']
            cadena = request.POST['inputTextCadena']
            context = {
                'query_three': get_query_three_pais_cadena(
                    fecha_inicio[-5:],
                    fecha_final[-5:],
                    fecha_final[:4],
                    pais,
                    cadena,
                ),
                'fecha_inicio': fecha_inicio,
                'fecha_final': fecha_final,
                'pais': pais,
                'cadena': cadena,
            }
        elif request.POST.get('inputTextPais', False):
            pais = request.POST['inputTextPais']
            context = {
                'query_three': get_query_three_pais(
                    fecha_inicio[-5:],
                    fecha_final[-5:],
                    fecha_final[:4],
                    pais,
                ),
                'fecha_inicio': fecha_inicio,
                'fecha_final': fecha_final,
                'pais': pais,
            }
        elif request.POST.get('inputTextCadena', False):
            print('hola')
            cadena = request.POST['inputTextCadena']
            context = {
                'query_three': get_query_three_cadena(
                    fecha_inicio[-5:],
                    fecha_final[-5:],
                    fecha_final[:4],
                    cadena,
                ),
                'fecha_inicio': fecha_inicio,
                'fecha_final': fecha_final,
                'cadena': cadena,
            }
        else:
            context = {
                'query_three': get_query_three(
                    fecha_inicio[-5:],
                    fecha_final[-5:],
                    fecha_final[:4]
                ),
                'fecha_inicio': fecha_inicio,
                'fecha_final': fecha_final,
            }
        return render(request, 'final_challenge/templates/tables/table_three.html', context)
    return render(request, 'final_challenge/templates/tables/table_three.html')


def query_four(request):
    """"El total de personas que vieron cada pelicula en centroamerica"""
    if request.method == 'POST':
        pelicula = request.POST['inputTextPelicula']
        print(pelicula)
        context = {
            'query_four': get_query_four(pelicula),
            'query_five': get_query_five(pelicula),
            'pelicula': pelicula,
        }
        return render(request, 'final_challenge/templates/tables/table_four.html', context)

    return render(request, 'final_challenge/templates/tables/table_four.html')


def query_five(requests):
    """El total de personas que vieron cada pelicula en centroamerica
    por cadena de cine"""
    context = {
        #'query_five': get_query_five()
    }
    return render(requests, 'final_challenge/templates/tables/table_five.html', context)


def query_six(request):
    """El total de personas que vieron cada pelicula en centroamerica
    por cadena de cine pero en porcentaje"""
    if request.method == 'POST':
        pelicula = request.POST['inputTextPelicula']
        context = {
            'query_six': get_query_six(pelicula),
            'pelicula': pelicula
        }
        return render(request, 'final_challenge/templates/tables/table_six.html', context)
    return render(request, 'final_challenge/templates/tables/table_six.html')


def query_seven(request):
    """Mostrar para cada pelicula el total de personas que acudieron a verla en la
    semana por pais y ordenarla de la más vista a la menos vista"""
    if request.method == 'POST':
        fecha_inicio = request.POST['inputFechaInicio']
        fecha_final = request.POST['inputFechaFinal']
        if request.POST.get('inputTextPelicula', False):
            pelicula = request.POST['inputTextPelicula']
            context = {
                'query_seven': get_query_seven(
                    fecha_inicio[-5:],
                    fecha_final[-5:],
                    fecha_final[:4],
                    pelicula
                ),
                'fecha_inicio': fecha_inicio,
                'fecha_final': fecha_final,
                'pelicula': pelicula,
            }
            return render(request, 'final_challenge/templates/tables/table_seven.html', context)
        else:
            context = {
                'movies': get_fecha_pelicula(
                    fecha_inicio[-5:],
                    fecha_final[-5:],
                    fecha_final[:4],
                ),
                'fecha_inicio': fecha_inicio,
                'fecha_final': fecha_final,
            }
            return render(request, 'final_challenge/templates/tables/table_seven.html', context)
    return render(request, 'final_challenge/templates/tables/table_seven.html')


def query_eight(request):
    """Total de personas por cadena de cine, por pais, por semana"""
    if request.method == 'POST':
        fecha_inicio = request.POST['inputFechaInicio']
        fecha_final = request.POST['inputFechaFinal']
        pais = request.POST['inputPais']
        pelicula = request.POST['inputTextPelicula']
        context = {
            'query_eight': get_query_eight(
                fecha_inicio[-5:],
                fecha_final[-5:],
                fecha_final[:4],
                pais,
                pelicula,
            ),
            'fecha_inicio': fecha_inicio,
            'fecha_final': fecha_final,
            'pais': pais,
            'pelicula': pelicula,
        }
        return render(request, 'final_challenge/templates/tables/table_eight.html', context)
    return render(request, 'final_challenge/templates/tables/table_eight.html')


def query_nine(request):
    """Total de personas por cadena de cine, por pais, por semana en porcentaje"""
    if request.method == 'POST':
        fecha_inicio = request.POST['inputFechaInicio']
        fecha_final = request.POST['inputFechaFinal']
        pais = request.POST['inputPais']
        if request.POST.get('inputTextPelicula', False):
            pelicula = request.POST['inputTextPelicula']
            context = {
                'query_nine': get_query_nine(
                    fecha_inicio[-5:],
                    fecha_final[-5:],
                    fecha_final[:4],
                    pais,
                    pelicula,
                ),
                'fecha_inicio': fecha_inicio,
                'fecha_final': fecha_final,
                'pais': pais,
                'pelicula': pelicula,
            }
        else:
            context = {
                'movies': get_fecha_pais_pelicula(
                    fecha_inicio[-5:],
                    fecha_final[-5:],
                    fecha_final[:4],
                    pais,
                ),
                'fecha_inicio': fecha_inicio,
                'fecha_final': fecha_final,
                'pais': pais,
            }
        return render(request, 'final_challenge/templates/tables/table_nine.html', context)
    return render(request, 'final_challenge/templates/tables/table_nine.html')
