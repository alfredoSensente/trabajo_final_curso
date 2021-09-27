"""Views de final_challenge"""
from django.shortcuts import render
from .services import get_query_one
from .services import get_query_four
from .services import get_query_two
from .services import get_query_three
from .services import get_query_five
from .services import get_query_six
from .services import get_query_seven
from .services import get_query_eight
from .services import get_query_nine


# Metodos


def fecha_hdp(request):
    """docstring"""
    if request.POST['inputFechaInicio']:
        fecha_inicio = request.POST['inputFechaInicio']
        if request.POST['inputFechaFinal']:
            fecha_final = request.POST['inputFechaFinal']
            if fecha_inicio[:4] == fecha_final[:4]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# Create your views here.

def query_one(request):
    """Formulario para ingresar los parametros para mostrar template table_one"""
    if request.method == 'POST':
        if fecha_hdp(request) is True:
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
        if fecha_hdp(request) is True:
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
        if fecha_hdp(request) is True:
            fecha_inicio = request.POST['inputFechaInicio']
            fecha_final = request.POST['inputFechaFinal']
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


def query_four(requests):
    """"El total de personas que vieron cada pelicula en centroamerica"""
    context = {
        'query_four': get_query_four()
    }
    return render(requests, 'final_challenge/templates/tables/table_four.html', context)


def query_five(requests):
    """El total de personas que vieron cada pelicula en centroamerica
    por cadena de cine"""
    context = {
        'query_five': get_query_five()
    }
    return render(requests, 'final_challenge/templates/tables/table_five.html', context)


def query_six(requests):
    """El total de personas que vieron cada pelicula en centroamerica
    por cadena de cine pero en porcentaje"""
    context = {
        'query_six': get_query_six()
    }
    print(context['query_six']['0'])
    return render(requests, 'final_challenge/templates/tables/table_six.html', context)


def query_seven(request):
    """Mostrar para cada pelicula el total de personas que acudieron a verla en la
    semana por pais y ordenarla de la más vista a la menos vista"""
    if request.method == 'POST':
        if fecha_hdp(request) is True:
            fecha_inicio = request.POST['inputFechaInicio']
            fecha_final = request.POST['inputFechaFinal']
            context = {
                'query_seven': get_query_seven(
                    fecha_inicio[-5:],
                    fecha_final[-5:],
                    fecha_final[:4]
                ),
                'fecha_inicio': fecha_inicio,
                'fecha_final': fecha_final,
            }
            return render(request, 'final_challenge/templates/tables/table_seven.html', context)
    return render(request, 'final_challenge/templates/tables/table_seven.html')


def query_eight(request):
    """Total de personas por cadena de cine, por pais, por semana"""
    if request.method == 'POST':
        if fecha_hdp(request) is True:
            fecha_inicio = request.POST['inputFechaInicio']
            fecha_final = request.POST['inputFechaFinal']
            pais = request.POST['inputPais']
            print(pais)
            context = {
                'query_eight': get_query_eight(
                    fecha_inicio[-5:],
                    fecha_final[-5:],
                    fecha_final[:4],
                    pais,
                ),
                'fecha_inicio': fecha_inicio,
                'fecha_final': fecha_final,
                'pais': pais,
            }
            return render(request, 'final_challenge/templates/tables/table_eight.html', context)
    return render(request, 'final_challenge/templates/tables/table_eight.html')

def query_nine(request):
    """Total de personas por cadena de cine, por pais, por semana en porcentaje"""
    if request.method == 'POST':
        if fecha_hdp(request) is True:
            fecha_inicio = request.POST['inputFechaInicio']
            fecha_final = request.POST['inputFechaFinal']
            pais = request.POST['inputPais']
            print(pais)
            context = {
                'query_nine': get_query_nine(
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
