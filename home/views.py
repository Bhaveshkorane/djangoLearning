from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("this is my server")

def aboutme(request):
    return render(request,"aboutme.html")

def myresume(request):
    return render(request,"my_resume.html")


text="""hello bhavesh this is your text that you are fetchning form the backend"""

student=[
    {'name':'Bhavesh', 'age':30},
    {'name':'Abhishek', 'age':20},
    {'name':'Sainath', 'age':15},
    {'name':'Adinath', 'age':25}
]



def fetchData(request):
    return render(request,"fetchData.html",context={'text':text,'student':student})



