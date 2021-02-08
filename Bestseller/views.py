from django.shortcuts import render
from .models import Bestseller

# Create your views here.
def bestseller(request):
    allbooks = Bestseller.objects.all()
    params = {'allbooks':allbooks}        
    return render(request, 'Bestseller/bestseller.html', params)

def readbook(request,title,slug):
    book = Bestseller.objects.get(slug=slug)
    param = {'book':book}
    return render(request, 'Bestseller/readbook.html',param)