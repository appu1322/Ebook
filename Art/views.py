from django.shortcuts import render
from .models import Art

# Create your views here.
def art(request):
    allbooks = Art.objects.all()
    params = {'allbooks':allbooks}        
    return render(request, 'Art/art.html', params)


def readbook(request,title,slug):
    book = Art.objects.get(slug=slug)
    param = {'book':book}
    return render(request, 'Art/readbook.html',param)