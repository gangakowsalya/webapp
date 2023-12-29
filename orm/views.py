from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
import json

from .models import test1

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to Home</h1>")

def registration(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)        
        obj = test1()
        obj.username = username
        obj.email = email
        obj.password = password
        obj.save()
        print("data saved succesfully",obj.username,obj.email,obj.password)        
        return redirect("read")
    else:
        return render(request,"registration.html",{})


def read(request):        
    data = test1.objects.all()
    return render(request,'read.html',{"data":data})

def update(request,id):
    getdata = test1.objects.get(id = id)  
    if request.method == "POST":
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)        
        getdata.username = username
        getdata.email = email
        getdata.password = password
        getdata.save()
        return redirect('read')   
    
    return render(request,"update.html",{"data":getdata})

def delete(request,id):
    getdata = test1.objects.get(id = id) 
    getdata.delete()
    return redirect("read")

def request(request):
    
    url = "https://magicpin.in/india/Madurai/All/Restaurant/Ice-Cream/"
    response = requests.get(url)

    try:
        # Check if the request was successful (status code 200)
        response.raise_for_status()
    
        # Extract the content from the response
        data = response.json()

        # Now 'data' contains the JSON content, and you can work with it
        print(data)

    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print ("Oops! Something went wrong:", err)
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
    

 
        
    return HttpResponse("<h1>Requests</h1>")
    