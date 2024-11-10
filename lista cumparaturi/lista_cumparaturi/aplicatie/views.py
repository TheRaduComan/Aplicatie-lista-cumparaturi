from django.shortcuts import render
from .models import Produs

def index(request):
    produse = Produs.objects.all()
    return render(request, 'index.html', {'produse': produse})

from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Produs

def adauga_produs(request):
    if request.method == 'POST':
        nume = request.POST['nume']
        produs = Produs(nume=nume)
        produs.save()
        return redirect('index')
    return render(request, 'adauga.html')

from django.shortcuts import get_object_or_404, redirect
from .models import Produs

def sterge_produs(request, id):
    produs = get_object_or_404(Produs, id=id)
    produs.delete()
    return redirect('index')

from django.shortcuts import get_object_or_404, redirect
from .models import Produs

def marcheaza_cumparat(request, id):
    produs = get_object_or_404(Produs, id=id)
    produs.cumparat = True
    produs.save()
    return redirect('index')

