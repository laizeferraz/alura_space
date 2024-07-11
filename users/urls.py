from django.urls import path
from .views import view_login, register, view_logout

urlpatterns = [
  path('login', view_login, name='login'),
  path('register', register, name='register'),
  path('logout', view_logout, name='logout'), 
]