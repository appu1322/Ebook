from django.urls import path
from . import views

urlpatterns = [
    path('education/', views.education , name='education'),
    path('education/<str:title>/<int:slug>/page=1', views.readbook , name='readbook'),
]