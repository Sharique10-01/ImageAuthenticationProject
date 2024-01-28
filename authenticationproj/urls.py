"""
URL configuration for authenticationproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from authenticationproj import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authenticationproj/add',views.add),
    path('authenticationproj/<int:id>',views.details),
    path('authenticationproj/',views.authenticationproj), # the default page isset to homepage now 
    path('authenticationproj/delete/<int:id>',views.delete),
    path('signin',views.signin),
    path('signup',views.signup),
    path('search/',views.search),
    path('',views.home)
]
