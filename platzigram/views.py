"""

Vistas de platzigram

"""
# Django
from django.urls import path
from django.http import HttpResponse
from django.http import JsonResponse

import json

# Utilities
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %d, %Y - %H:%M horas')
    #now = str(now)
    return HttpResponse('Hola Mundo!! Hora local del servidor es {}'
        .format(now))

def sort_integers(request):
    # Devuelve una respuesta JSON con enteros en orden
    #debugger
    # import pdb

    # http://localhost:8000/saludo/?numbers=10,4,5,32

    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Enteros ordenados satisfactoriamente'
    }
    return HttpResponse(json.dumps(data, indent=4),
        content_type = 'application/json')

""" OTRA FORMA
    numbers = request.GET['numbers']
    pdb.set_trace()
    numbers = numbers.split(',')
    numbers = [int(x) for x in numbers]

    return JsonResponse('Hola! Estos son los numeros: {}'.format(sorted(numbers)), safe=False)
"""



def say_hi(request, name, age):
    #Regresa un saludo
    if age < 12:
        message = 'Lo siento {}, no puedes estar acá'.format(name)
    else:
        message = 'Hola {}, bienvenid@ a Platzigram!'.format(name)

    return HttpResponse(message)
