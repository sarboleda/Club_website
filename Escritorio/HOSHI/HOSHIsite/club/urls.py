from django.urls import path
from club import views

urlpatterns = [
    path('' , views.index, name='index'),
    path('home/' , views.home, name='home'),
]