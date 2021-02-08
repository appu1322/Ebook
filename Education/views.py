from django.shortcuts import render
from .models import Education

# Create your views here.
def education(request):
    allbooks = Education.objects.all()
    params = {'allbooks':allbooks} 
    return render(request, 'Education/education.html',params)

def readbook(request,title,slug):
    book = Education.objects.get(slug=slug)
    param = {'book':book}
    return render(request, 'Education/readbook.html',param)