from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

def index(request):
    context= {
        "variable1" : "Kmaal ka website hai",
        "variable3" : "Abhishek",
        "variable2" : "Great stuff"
        }
    # messages.success(request,"Success")
    return render(request,'index.html', context)
    
    #return HttpResponse("This is a homepage")
def loggedin_success(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"loggedin.html")

def loginuser(request):
    if request.user.is_anonymous: #to check if a user is already loggedin then render the logged in success page else authenticate the user

        if request.method=="POST":
                uname=request.POST.get("username")
                pwd=request.POST.get("password")
                print(uname,pwd)
                user=authenticate(username=uname,password=pwd)
            
                if user is not None:
                    login(request,user)
                    return redirect("/loggedin")
        return render(request,"login.html")
    return redirect("/loggedin")

def logoutuser(request):
    logout(request)
    return redirect("/")


def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is a about page")

def contact(request):
    if request.method=="POST":
        name =request.POST.get("name")
        email =request.POST.get("email")
        phone =request.POST.get("phone")
        desc =request.POST.get("desc")
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your form has been sent successfully!')

    #return HttpResponse("This is a contact page")
    return render(request,'contact.html')


