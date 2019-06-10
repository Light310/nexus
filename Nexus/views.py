import os
import time
import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def home(request):
    return render(request, 'templates/home.html', {})


def set_speed(request):
    speed = request.GET.get('speed')
    try:
        with open('files/speed.txt', 'w') as f:
            f.write(speed)
        response = json.dumps({'error': False, 'data': 'Ok'}, indent=2)
    except Exception as e:
        response = json.dumps({'error': True, 'message': str(e)}, indent=2)

    return HttpResponse(response, content_type='application/json')

def get_speed(request):
    with open('files/speed.txt', 'r') as f:
        speed = f.readline()
    return JsonResponse({'speed': speed})

def command(request):
    com = request.GET.get('com')
    file = os.path.join('files', 'command.txt')

    try:
        millis = int(round(time.time() * 1000))
        with open(file, 'w') as f:
            f.write('{0}:{1}'.format(millis, com))
        print('Wrote {0} as command at {1}'.format(com, millis))
        response = json.dumps({'error': False, 'data': 'Ok'}, indent=2)
    except Exception as e:
        response = json.dumps({'error': True, 'message': str(e)}, indent=2)

    return HttpResponse(response, content_type='application/json')


def read_command(request):
    file = os.path.join('files', 'command.txt')

    try:
        with open(file) as f:
            data = f.read().split(':')
        millis_prev = int(data[0])
        command = data[1]
        millis_cur = int(round(time.time() * 1000))
        if millis_cur - millis_prev > 1000:
            data = 'None'
        else:
            data = command
        print('Read command : {0}'.format(data))
        response = json.dumps({'error': False, 'data': data}, indent=2)
    except Exception as e:
        response = json.dumps({'error': True, 'message': str(e)}, indent=2)

    return HttpResponse(response, content_type='application/json')