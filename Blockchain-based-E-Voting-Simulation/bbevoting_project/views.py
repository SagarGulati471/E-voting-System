from django.shortcuts import render



def polls(request):
    return render(request,'polls.html')