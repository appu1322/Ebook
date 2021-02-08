from django.urls import path
from . import views

urlpatterns = [
    path('fantacy/', views.fantacy , name='fantacy'),
    path('fantacy/<str:title>/<int:slug>/page=1', views.readbook , name='readbook'),
]