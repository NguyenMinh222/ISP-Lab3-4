from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4>Hello, everyone, it is my first Django project</h4>")
