from django.urls import path
from django.conf.urls import url
from .views import login_view
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('login_view', login_view),
]