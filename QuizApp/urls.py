"""QuizApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from logins.views import login, logout
from django.conf.urls.static import static 
from QuizApp.settings import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_ROOT,MEDIA_URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('quiz.urls','quiz'), namespace='quiz')),
    path('', include(('logins.urls','logins'), namespace='logins')),
    path('login/', login,name='login'),
    path('logout/', logout,name='logout'),
    path('home/',include(('home.urls','home'),namespace='home')),
    path('',include(('register.urls','register'),namespace='register')),
    path('logins/',include('logins.urls')),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

    