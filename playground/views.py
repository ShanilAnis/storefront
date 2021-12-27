from django.shortcuts import render
from django.http import HttpResponse

def say_hello(requests):
    x = 1
    x = 2
    
    return render(requests, 'hello.html', {"name": 'Shanil'})