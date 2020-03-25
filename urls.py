from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('intimateuser/', views.intimateuser, name='intimateuser'),
    path('login/',views.login, name='login'),
]