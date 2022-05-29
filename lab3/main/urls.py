"""Отслеживаем переход на главную страницу"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('About-us', views.about, name='about'),
    path('Add_a_dish', views.create, name='create'),
    path('login', views.loginpage, name='login_page'),
    path('logout', views.logout_user, name='logout_user'),
    path('Register', views.register, name='register_page'),
    path('popup', views.popup, name='popup_window'),
    path('menu', views.menu, name='menu_page')


]

