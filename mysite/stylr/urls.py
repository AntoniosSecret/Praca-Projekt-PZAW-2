from django.urls import path
from . import views

app_name = 'stylr'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('login/', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register_user'),
    path('profile/', views.profile, name='profile'),
]