from django.shortcuts import render
from.models import Stories

# Create your views here.
def stories(request):
    allbooks = Stories.objects.all()
    params = {'allbooks':allbooks}        
    return render(request, 'Stories/stories.html', params)


def readbook(request,title,slug):
    book = Stories.objects.get(slug=slug)
    param = {'book':book}
    return render(request, 'Stories/readbook.html',param)