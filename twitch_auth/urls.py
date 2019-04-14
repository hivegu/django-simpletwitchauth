from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login_twitch'),
    path('callback/', views.callback, name='callback_twitch'),
    path('logout/', views.logout, name='logout'),
]
