from django.shortcuts import render, HttpResponse
from . import model
# Create your views here.
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


