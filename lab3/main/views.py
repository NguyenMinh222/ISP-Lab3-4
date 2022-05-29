from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login_page')
def index(request):
    return render(request, 'main/home.html', {'title': 'О готовке'})


@login_required(login_url='login_page')
def about(request):
    return render(request, 'main/about.html')


@login_required(login_url='login_page')
def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_page')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('popup_window')
        else:
            form = CreateUserForm()

    contex = {'form': form}
    return render(request, 'main/register_page.html', contex)


"""Проверка набора учета данных с authenticate"""


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
     if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            """с помощью метода login и выполняется вход """
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Пароль или имя пользователя был введён неправильно!')

     contex = {}
     return render(request, 'main/login_page.html', contex)


def logout_user(request):
    logout(request)
    return redirect('login_page')


def popup(request):
    return render(request, 'main/popup_window.html')


def menu(request):
    tasks = Task.objects.order_by('-id')  # получаем все оъекты из класса
    return render(request, 'main/menu_page.html', {'tasks': tasks})
