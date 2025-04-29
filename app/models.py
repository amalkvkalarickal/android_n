from django.db import models

# Create your models here.



class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)
    
    
class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    district=models.CharField(max_length=200)   
    pincode=models.CharField(max_length=200)
    house_no=models.CharField(max_length=200)
    phone_no=models.CharField(max_length=200)  