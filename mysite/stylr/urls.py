from django.urls import path
from . import views

app_name = 'stylr'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create')
]