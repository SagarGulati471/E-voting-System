from django.db import models

# Create your models here.

class Register(models.Model):
    first_name=models.CharField(max_length=50,blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    email=models.CharField(max_length=50,blank=True)
    phone_no=models.CharField(max_length=50,blank=True)
    aadhar=models.CharField(max_length=50,blank=True)
    voter_id=models.CharField(max_length=50,blank=True)
    Address=models.CharField(max_length=50,blank=True)
    inputCity=models.CharField(max_length=50,blank=True)
    inputZip=models.CharField(max_length=50,blank=True)
    id_proof=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.first_name