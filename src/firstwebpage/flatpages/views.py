from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "static_handler.html")


def template_page(request):
    return render(request, "index.html")


def hello(request):
    return HttpResponse("Привет, Мир!")


def hello_plain(request):
    return HttpResponse("Привет, Мир!", content_type="text/plain; charset=utf-8")
