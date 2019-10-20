import os
import time
import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def home(request):
    return render(request, 'templates/home.html', {})       

def view_stream(request):
    return render(request, 'templates/view-stream.html', {})

def set_speed(request):
    speed = request.GET.get('speed')
    file = os.path.join('files', 'speed.txt')
    try:
        with open(file, 'w') as f:
            f.write(speed)
        response = json.dumps({'error': False, 'data': 'Ok'}, indent=2)
    except Exception as e:
        response = json.dumps({'error': True, 'message': str(e)}, indent=2)

    return HttpResponse(response, content_type='application/json')

def get_speed(request):
    file = os.path.join('files', 'speed.txt')
    with open(file, 'r') as f:
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
    file = '/nexus/files/command.txt'

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


def get_fenix_data(request):
    file = os.path.join('files', 'data.txt')

    try:
        with open(file) as f:
            file_data = json.loads(f.read())
        millis_prev = int(file_data['millis'])                       
        millis_cur = int(round(time.time() * 1000))
        data = file_data['data']
        if millis_cur - millis_prev > 1000:
            for k in data:
                data[k] = 0.0
        response = json.dumps({'error': False, 'data': data}, indent=2)
    except Exception as e:
        response = json.dumps({'error': True, 'message': str(e)}, indent=2)

    return HttpResponse(response, content_type='application/json')


def get_batteries_values(request):
    file = os.path.join('files', 'batteries.txt')

    try:
        with open(file) as f:
            data = f.read().split(':')
        millis_prev = int(data[0])                       
        millis_cur = int(round(time.time() * 1000))
        if millis_cur - millis_prev > 1000:
            pi, pi_pct, servo, servo_pct = 0.0, 0.0, 0.0, 0.0
        else:
            pi, pi_pct, servo, servo_pct = data[1].split(',')
        response = json.dumps({'error': False, 'pi': pi, 'pi_pct': pi_pct, 'servo': servo, 'servo_pct': servo_pct}, indent=2)
    except Exception as e:
        response = json.dumps({'error': True, 'message': str(e)}, indent=2)

    return HttpResponse(response, content_type='application/json')


def get_gyroaccel_data(request):
    file = os.path.join('files', 'gyroaccel.txt')

    try:
        with open(file) as f:
            data = f.read().split(':')
        millis_prev = int(data[0])
        millis_cur = int(round(time.time() * 1000))
        if millis_cur - millis_prev > 1000:
            x, y, z = 0.0, 0.0, 0.0
        else:
            x, y, z = data[1].split(',')
        response = json.dumps({'error': False, 'x': x, 'y': y, 'z': z}, indent=2)
    except Exception as e:
        response = json.dumps({'error': True, 'message': str(e)}, indent=2)

    return HttpResponse(response, content_type='application/json')
