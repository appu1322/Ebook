from django.shortcuts import render
from .models import Fantacy

# Create your views here.
def fantacy(request):
    allbooks = Fantacy.objects.all()
    params = {'allbooks':allbooks} 
    print('hiiii')
    return render(request, 'Fantacy/fantacy.html',params)

def readbook(request,title,slug):
    book = Fantacy.objects.get(slug=slug)
    param = {'book':book}
    return render(request, 'Fantacy/readbook.html',param)