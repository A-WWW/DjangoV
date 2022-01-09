from django.http import HttpResponse, HttpResponseNotFound, Http404

from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "Site subject", 'url_name': 'about'},
        {'title': "Add object", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        {'title': "To come in", 'url_name': 'login'}
]

def index(request):
    posts = Object.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Home page',
        'cat_selected': 0,
    }
    return render(request, 'object/index.html', context = context)



# def about(request):
#     return render(request, 'r:/Django_1/DjangoV/stroke/object/templates/object/about.html', {'menu': menu,
#                                                                                              'title': 'Page title 1'})


def about(request):
    return render(request, 'object/about.html', {'menu': menu, 'title': 'Page title 1'})


def addpage(request):
    return HttpResponse("Add object")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"vizio c id {post_id}")


def show_category(request, cat_id):
    posts = Object.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Display by capability',
        'cat_selected': cat_id,
    }

    return render(request, 'object/index.html', context=context)

def pageNotFound(requst, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')