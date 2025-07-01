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
        return render(request, 'home.html')


def RegisterView(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        messages.success(request, "Registration successful. You can now log in.")
        return redirect('login')
    else:
         return render(request, 'register.html')

def LoginView(request):
    return render(request, 'login.html')