from django.shortcuts import render
from .models import Game


def platform(request):
    return render(request, 'task1/platform.html')

def games(request):
    game_list = Game.objects.all()
    return render(request, 'task1/games.html', {'games': game_list})

def cart(request):
    return render(request, 'task1/cart.html')

from .forms import UserRegister
from .models import Buyer

users = ['user1', 'user2', 'user3']

def register(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, balance=0.0, age=age)
                return render(request, "task1/success.html", {'message': f'Приветствуем, {username}!'})
        else:
            info['form'] = form
    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'task1/registration_page.html', info)