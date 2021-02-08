from django.urls import path
from . import views

urlpatterns = [
    path('bestseller/', views.bestseller , name='bestseller'),
    path('bestseller/<str:title>/<int:slug>/page=1', views.readbook , name='readbook'),
]