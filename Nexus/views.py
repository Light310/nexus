from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'templates/home.html', {})


def get_command(request):
    with open('files/command.txt', 'r') as f:
        command = f.readline()
    return JsonResponse({'command': command})

def get_speed(request):
    with open('files/speed.txt', 'r') as f:
        speed = f.readline()
    return JsonResponse({'speed': speed})