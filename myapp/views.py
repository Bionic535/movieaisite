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
