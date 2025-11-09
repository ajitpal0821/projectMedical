from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
import os
import hashlib
from app1.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    # we are applying condition for the form
    if request.method=='POST':
       username=request.POST.get('name')
       useremail=request.POST.get('email')
       userphone=request.POST.get('phone')
       usersubject=request.POST.get('subject')
       usermessage=request.POST.get('message')

       userdata= contactusdata(name=username,email=useremail,phone=userphone,subject=usersubject,message=usermessage)
       userdata.save()
       return redirect('/contactus/')
    else:
        return render(request,'contactus.html')

def blog(request):
    return render(request,'blog.html')

def appointment(request):
    if request.method=='POST':
      username=request.POST.get('name')
      emailid=request.POST.get('email')
      phoneno=request.POST.get('phone')
      depart=request.POST.get('department')
      apdate=request.POST.get('cdate')
      doctor=request.POST.get('doctor')
      usermessage=request.POST.get('message')
      userappoint=appointdata(apname=username,apemail=emailid,apphone=phoneno,apdepart=depart,apdate=apdate,apdoctor=doctor,apmessage=usermessage)
      userappoint.save()
      return redirect('/appointment/')
    else:
        return render(request,'appointment.html')
    
def signup(request):
    return render(request,'signup.html')

def registerdata(request):
    if request.method=='POST':
        userfirstname=request.POST.get('firstname')
        userlastname=request.POST.get('lastname')
        useremail=request.POST.get('email')
        useremail = useremail.lower()
        userphone=request.POST.get('phone')
        userpassword=request.POST.get('password')
        userconfirmpassword=request.POST.get('confirmpswd')

        if(userpassword==userconfirmpassword):
            hashed_password = hashlib.md5(userpassword.encode()).hexdigest()
            usersignup=registerdataa(regfname=userfirstname, reglname=userlastname,regemail=useremail,regphone=userphone,regpassword=hashed_password)
            usersignup.save()
            return redirect('/signup/')
        else:
            return HttpResponse("<h1>password and confirm password does not match </h1>")
    else:
        return render(request,'signup.html')
    # 05-04-24
def login(request):
    return render(request,'login.html')

def logindata(request):
    if request.method=='POST':
        user_useremail=request.POST.get('useremail')
        user_useremail = user_useremail.lower()
        # code for converting characters to lower case in the database
        user_userpassword=request.POST.get('userpassword')
        # this is for encoding and MD5 cannot be decoded
        # 09-04-2024
        password_md5 = hashlib.md5(user_userpassword.encode()).hexdigest()
        user = registerdataa.objects.filter(regemail=user_useremail, regpassword=password_md5).first()
        if user:
            # Login successful, perform necessary actions (e.g., set session)
            return redirect('/')
        else:
           
            error = ['Invalid Emailid or Password']
            return render(request, 'login.html', {'my_static_list': error})
            
        # 09-04-2024
