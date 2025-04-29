from django.http import JsonResponse
from django.shortcuts import render
from .models import *

# Create your views here.



def apireg(request):
    data=[]
    username=request.GET.get('uname')
    password=request.GET.get('password')
    fname=request.GET.get('fname')
    lname=request.GET.get('lname')
    email=request.GET.get('email')
    pin=request.GET.get('pin')
    place=request.GET.get('place')
    dist=request.GET.get('district')
    hno=request.GET.get('hno')
    phone=request.GET.get('phone')
    
    try:
        ob=login.objects.filter(username=username)
        if ob:
            status = "error"
            message="Username Already Exists!!"
        else:
            obj=login(username=username,password=password,usertype='user')
            obj.save()
            
            obj1=user(first_name=fname,last_name=lname,email=email,place=place,district=dist,pincode=pin,house_no=hno,phone_no=phone,login_id=obj.pk)
            obj1.save()
            if obj1:
                status = "success"
            else:
                status = "error"
    except login.DoesNotExist:
        status = "error"
        message="Failed"
        
    response = {
        
       'status': status,
        'data': data
    }
    if status == "error":
        response['message'] = message 
    
    return JsonResponse(response)  
