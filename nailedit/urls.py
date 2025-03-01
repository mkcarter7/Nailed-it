"""nailedit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import include
from rest_framework import routers
from naileditapi.views.room import RoomView
from naileditapi.views.tool import ToolView
from naileditapi.views.material import MaterialView
from naileditapi.views.project import ProjectView
from django.urls import path

#USE BUILT IN CLASS IN DJANO SO THE SERVER RESPONDS WITH APPRORIATE METHOD
#DFR SETS THE RESOURCE FOR EACH METHOD IN THE VIEW
#TRUE/FALSE TELLS ROUTER TO TO ACCEPT 'AUTHORS'/'BOOKS'/'GENRE'
#1ST PARAM SETS UP URL, 2ND TELLS SERVER WHICH URL, 3RD BASE NAME OR NICK NAME-SINGULAR VERSION OF URL
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'rooms', RoomView, 'rooms')
router.register(r'materials', MaterialView, 'materials')
router.register(r'tools', ToolView, 'tools')
router.register(r'project', ProjectView, 'projects')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    router.register(r'projectviews', ProjectView, 'projectview')
]
