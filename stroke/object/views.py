from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .forms import *
from .models import *
from .utils import *

menu = [{'title': "Site subject", 'url_name': 'about'},
        {'title': "Add object", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        {'title': "To come in", 'url_name': 'login'}
]


class ObjectHome(DataMixin, ListView):
    model = Object
    template_name = 'object/index.html'
    context_object_name = 'posts'
    allow_empty = False


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main page")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Object.objects.filter(is_published=True).select_related('cat')

# def index(request):
#     posts = Object.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Home page',
#         'cat_selected': 0,
#     }
#     return render(request, 'object/index.html', context = context)


def about(request):
    contact_list = Object.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'object/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'Site subject'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'object/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add object")
        return dict(list(context.items()) + list(c_def.items()))



# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'object/addpage.html', {'form': form,  'menu': menu, 'title': 'Add object'})


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'object/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Feedback")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')
#
# def login(request):
#     return HttpResponse("Авторизация")

def show_post(request, post_id):
    post = get_object_or_404(Object, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'object/post.html', context=context)


class ObjectCategory(DataMixin, ListView):
    model = Object
    template_name = 'object/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Object.objects.filter(cat__id=self.kwargs['cat_id'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Possibilities - ' + str(context['posts'][0].cat), cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


def show_category(request, cat_id):
    posts = Object.objects.filter(cat_id=cat_id)


    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Display by capability',
        'cat_selected': cat_id,
    }

    return render(request, 'object/index.html', context=context)


def pageNotFound(requst, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'object/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registration")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'object/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authorization")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')
