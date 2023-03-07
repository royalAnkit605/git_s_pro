from django.shortcuts import render
from django.http import HttpResponse
def argentina(request):
    return HttpResponse('<h1><marquee>Vamossss Argentina</h1></marquee>')
