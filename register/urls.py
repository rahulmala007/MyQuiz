from django.urls import path
from django.conf.urls import url
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', start_view),
    path('registerUser',register_view,name='register_user'),
    
]