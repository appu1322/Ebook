from django.urls import path
from . import views

urlpatterns = [
    path('art/', views.art , name='art'),
    path('art/<str:title>/<int:slug>/page=1', views.readbook , name='readbook'),
]