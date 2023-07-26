from app.models import *
from django.shortcuts import render
from django.http import HttpResponse

def insert_topic(request):
    TN=input('Enter your Topicname : ')
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()
    return HttpResponse('topic data insertion is done')

def insert_webpage(request):
    TN=input('enter topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()
    n=input('enter name : ')
    u=input('enter url : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save() 
    return HttpResponse('webpage data insertion is done')

def insert_accessrecord(request):
    TN=input('enter topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()
    n=input('enter name : ')
    u=input('enter url : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()

    d=input('enter date :  ')
    a=input('enter author :  ')
    AO=Accessrecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()
    return HttpResponse('accessrecord data is done')


def display_Topic(request):
    TO=Topic.objects.all()
    d={'TO':TO}
    return render(request,'display_Topic.html',d)


def display_webpage(request):
    WO=Webpage.objects.all()
    d={'WO':WO}
    return render(request,'display_webpage.html',d) 


def dispaly_accessrecord(request):
    AO=Accessrecord.objects.all()
    d={'AO':AO}
    return render(request,'dispaly_accessrecord.html',d)
