"""
URL configuration for project38 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
from app.models import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_topic/',insert_topic,name='insert_topic'),
    path('insert_webpage/',insert_webpage,name='insert_webpage'),
    path('insert_accessrecord/',insert_accessrecord,name='insert_accessrecord'),
    
    
    path('display_Topic/',display_Topic,name='display_Topic'),
    path('display_webpage/',display_webpage,name='display_webpage'),

    path('dispaly_accessrecord/',dispaly_accessrecord,name='dispaly_accessrecord'),
   
] 
