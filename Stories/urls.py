from django.urls import path
from . import views

urlpatterns = [
    path('stories/', views.stories , name='stories'),
    path('stories/<str:title>/<int:slug>/page=1', views.readbook , name='readbook'),
]