from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Signup
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail 


# Create your views here.


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        print('*'*40)
        #print(username,first_name,last_name,email,password1,password2)
        #return HttpResponse('this is the signup cpage')
        if password1==password2:

            if User.objects.filter(username=username).exists():
                #print("Username Problem--"*5)
                messages.error(request,"Sorry the Username already exists !")
                return redirect('/')
                

            elif User.objects.filter(email=email).exists():
                messages.error(request,"The email is already registered")
                #print("Email Problem--"*3)
                return redirect('/')
            
            else:
                user=User(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                #print("Registered-"*5)
                messages.error(request,"You are registered successfully !")
                
                send_mail('Reply from Team BT5-184',
        'Thanks '+ first_name + ' Your information is submitted. You will be given your voter Id soon after verification process is completed.\nHappy Voting :) \n ',
        'sagargulati84@gmail.com',
        [email,'sagargulati471@gmail.com'],
        fail_silently=False)

                return redirect('/')
               
        messages.error(request,"Passwords mismatched")
        return redirect('/')
#Else part for not a post request is not written    




def login(request):
    if request.method=='POST':
        username=request.POST['loginusername']
        password=request.POST['loginpass']
        print(username,password)
        user=authenticate(request,username=username,password=password)
        print(user)

        if user is not None:
            login(request,user)
            messages.info(request,'You are loggeed in successfully !')
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials Entered')
            return redirect('/')
        print('*'*35)
        print(username,password)
        
    return HttpResponse('It is login page')

    '''

        if User.objects.filter(username=username,password=password).exists():
            auth.login(request,user)
            messages.info(request,'You are loggeed in successfully !')
            return redirect('/')  
        else:
            messages.info(request,'Invalid Credentials Entered')
            return redirect('/')
            
        '''