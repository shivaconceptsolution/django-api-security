from django.http import HttpResponse
from django.shortcuts import render
import requests
def index(request):
    url = 'http://127.0.0.1:8000/api/insert-data/'
    headers = {
    'Authorization': 'Token 331bdff98e17b4128c868290e7844ad8c546c711',
    'Content-Type': 'application/json'
         }
    data = {'name': 'Example','value': 123}
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(response.json())
    return render(request,"helloapp/hello.html",{"key":response.json()})
def addition(request):
    if request.method=="POST":
       a,b=request.POST.get("txtnum1"),request.POST.get("txtnum2")
       c=int(a)+int(b)
       return render(request,"helloapp/addition.html",{"key":"result is "+str(c)})
    else:
        return render(request,"helloapp/addition.html")
    
def sicalc(request):
    if request.method=="POST":
       p,r,t = request.POST.get("txtnum1"),request.POST.get("txtnum2"),request.POST.get("txtnum3")
       si = (float(p)*float(r)*float(t))/100
       return render(request,"helloapp/si.html",{"key":"result is "+str(si)})
    else:
        return render(request,"helloapp/si.html")

