from django.db import models

# Create your models here.
class Registeration(models.Model):  #step 5 need to creaet all fields and insert html file in templates
    #name=models.CharField(max_length=50) # create a new file urls.py in appname
    email=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=8)
# Create your models here

class hadmin(models.Model):  #step 5 need to create all fields and insert html file in templates
    name=models.CharField(max_length=50) # create a new file urls.py in appname
    email=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=8)

class userprofile(models.Model):  #step 5 need to creaet all fields and insert html file in templates
    firstname=models.CharField(max_length=30) # create a new file urls.py in appname
    lastname=models.CharField(max_length=30)
    dob=models.DateField()
    healthissue=models.CharField(max_length=30,default="no")
    interest=models.CharField(max_length=30,default="no")
    hobby=models.CharField(max_length=30,default="no")
    phone=models.CharField(max_length=13,default="no")    
    economic_pref=models.CharField(max_length=30,default="moderate")
    email=models.CharField(max_length=30)

class myrecord(models.Model):
    hospitalname=models.CharField(max_length=50)
    doctorname=models.CharField(max_length=50)
    hospitallocation=models.CharField(max_length=250)
    diseasename=models.CharField(max_length=50)
    documentname=models.CharField(max_length=50)
    file=models.FileField(blank=True, null=True)
    prescription=models.FileField(blank=True, null=True)
    description=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    date=models.DateField(auto_now=True)

class prescription(models.Model):
    prescrip_name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    diseasename=models.CharField(max_length=50)
    #medicinename=models.FileField()
    meal=models.CharField(max_length=10)
    time=models.TimeField(auto_now=False, auto_now_add=False)
    email=models.CharField(max_length=30)

class emergency(models.Model):
    hospitalname=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    phone=models.CharField(max_length=14)
    speciality=models.CharField(max_length=50,default="Multispeciality")