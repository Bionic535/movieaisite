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
from .models import *
from django.http import JsonResponse
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def movie_titles(request):
    csv_path = os.path.join(os.path.dirname(__file__), 'static', 'movie_dataset.csv')
    df = pd.read_csv(csv_path)
    # Adjust the column index or name as needed
    titles = df.iloc[:, 7].dropna().astype(str).str.strip().tolist()
    return JsonResponse({'titles': titles})

def home(request):
    return render(request, "home.html")
   
def films(request):
    if request.method == 'POST':
        name = request.POST.get('movie')
        numb = request.POST.get('numb')
        context = []
        try:
            name = str(name)
            numb = int(numb)
            context = model.model(name, numb - 1)
        except ValueError:
            name = None
            numb = None

        return render(request, 'films.html', {'films': context})
    else:
        return render(request, 'home')

def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("my-login")
            
    
    
    
    context = {'registerform': form}
    
    return render(request, "register.html", context=context)

def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("home")
    
    context = {'loginform':form}
    
    return render(request, "my-login.html", context=context)



def user_logout(request):
    auth.logout(request)
    return redirect("home")