from django.shortcuts import render, HttpResponse
from . import model
import os
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from urllib.parse import urlencode
from .models import *
from .models import UserFilmList
from django.http import JsonResponse
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def movie_titles(request):
    csv_path = os.path.join(os.path.dirname(__file__), 'static', 'movie_dataset.csv')
    df = pd.read_csv(csv_path, encoding='utf-8')
    # Adjust the column index or name as needed
    titles = df.iloc[:, 7].dropna().astype(str).str.strip().tolist()
    return JsonResponse({'titles': titles})

def home(request):
    return render(request, "home.html")
   
def films(request):
    context = []
    name = request.POST.get('movie') or request.session.get('movie')
    numb = request.POST.get('numb') or request.session.get('numb')

    # Clear session variables after use
    if 'movie' in request.session:
        del request.session['movie']
    if 'numb' in request.session:
        del request.session['numb']
        
    if request.user.is_authenticated:
        user_film_list = UserFilmList.objects.get(username=request.user.username)
    else:
        user_film_list = UserFilmList.objects.get(username="no_user")


    if name and numb:
        try:
            name = str(name)
            numb = int(numb)
            context = model.model(name, numb - 1)
        except (ValueError, TypeError):
            context = []
    
    return render(request, 'films.html', {'films': context, 'movie': name, 'numb': numb, 'list': user_film_list.film_ids, 'film_titles': user_film_list.film_titles})

def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'Email already exists.')
            else:
                #create film list
                user_film_list = UserFilmList.objects.create(
                    username = username,
                    film_ids=[]
                )
                form.save()
                return redirect("my-login")
        else:
            # Add form errors to the context
            context = {'registerform': form}
            return render(request, "register.html", context=context)
            
    context = {'registerform': form}
    
    return render(request, "register.html", context=context)

def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password.")

    context = {'loginform':form}
    
    return render(request, "my-login.html", context=context)


def user_logout(request):
    auth.logout(request)
    return redirect("home")

@login_required
def add_to_list(request):
    if request.method == "POST":
        film_to_add = request.POST.get('film')
        movie = request.POST.get('movie')
        numb = int(request.POST.get('numb'))

        username = request.user.username
        user_film_list = UserFilmList.objects.get(username=username)
        
        if len(user_film_list.film_ids) < 20:
            user_film_list.add_film(film_to_add)

        if movie and numb:
            request.session['movie'] = movie
            request.session['numb'] = numb
            return redirect('films')
        else:
            return redirect('home')
    return redirect('home')

@login_required
def remove_from_list(request):
    if request.method == "POST":
        film_to_add = request.POST.get('film')
        movie = request.POST.get('movie')
        numb = int(request.POST.get('numb'))

        username = request.user.username
        user_film_list = UserFilmList.objects.get(username=username)
        user_film_list.remove_film(film_to_add)

        if movie and numb:
            request.session['movie'] = movie
            request.session['numb'] = numb
            return redirect('films')
        else:
            return redirect('home')
    return redirect('home')


@login_required
def watchlist(request):
    username = request.user.username
    user_film_list = UserFilmList.objects.get(username=username)
    films = user_film_list.film_ids
    context = {'films': films}

    return render(request, "watchlist.html", context)


@login_required
def remove_from_watchlist(request):
    if request.method == "POST":
        film_to_remove = (request.POST.get('film'))
        
        username = request.user.username
        user_film_list = UserFilmList.objects.get(username=username)
        print(film_to_remove)
        user_film_list.remove_film(film_to_remove)
        context = {'films': user_film_list.film_ids}

        return render(request, "watchlist.html", context=context)
    return redirect('watchlist')
