from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from Bestseller.models import Bestseller
from Education.models import Education
from Fantacy.models import Fantacy
from Art.models import Art
from Stories.models import Stories


# Create your views here.
def index(request):
    category = ['bestseller', 'education', 'fantacy', 'art', 'stories'] 
    params = {}
    book1 = Bestseller.objects.all()
    book2 = Education.objects.all()
    book3 = Fantacy.objects.all()
    book4 = Art.objects.all()
    book5 = Stories.objects.all()
    books_queryset = [book1, book2, book3, book4, book5]    
    for i in books_queryset:
        allbooks = []
        start_index = (len(i)-1)
        last_index = (len(i)-6)
        if last_index<0:
            last_index = -1
        for j in range(start_index,last_index,-1):
            allbooks.append(i[j])
        params[category[0]] = allbooks
        category.pop(0)
    return render(request, 'Home/index.html', params)
