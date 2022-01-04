from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Object")


def categories(request, catid):
    if (request.POST):
        print(request.POST)
    return HttpResponse(f"<h1>Information by category</h1><p>{catid}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Yearly data</h1>{year}</p>")