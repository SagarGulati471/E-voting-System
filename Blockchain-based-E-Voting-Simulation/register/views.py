from django.shortcuts import render,redirect
from .models import Register
from django.contrib import messages
from django.core.mail import send_mail 

# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST['first_name']
        Last_name=request.POST['last_name']
        Email=request.POST['email']
        Phone_no=request.POST['phone_no']
        Aadhar=request.POST['aadhar']
        Voter_id=request.POST['voter_id']
        Address=request.POST['Address']
        print("************************",Address)
        #InputCity=request.POST['input_city']
        #print("************************",InputCity)
        #InputZip=request.POST['inputZip']
        #Id_proof=request.POST['id_proof']
        voter=Register(first_name=name, last_name= Last_name, email= Email , phone_no=Phone_no,aadhar=Aadhar, voter_id=Voter_id, Address= Address )  
        voter.save() 


        send_mail('Reply from Team BT5-184',
        'Thanks '+ name.split()[0] + ' for contacting us. We will reply you soon. ',
        'sagargulati84@gmail.com',
        [Email,'sagargulati471@gmail.com'],
        fail_silently=False)
        
        messages.error(request,"Your information is submitted successfully !")
        print("till here *********************")
        return render(request,'register.html')


        return redirect('')
    else:   
        return render(request,'register.html')
