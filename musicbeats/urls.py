
from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signup/success/', views.signup_success, name='signup_success'),
    path('songs/',views.songs,name='songs'),
    path('songs/<int:id>',views.songpost,name='songpost'),
] 
