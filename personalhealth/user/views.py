
# Create your views here.
from django.shortcuts import render,redirect
from .models import Registeration,userprofile,myrecord,prescription,hadmin,emergency
from django.http.response import HttpResponse
from .forms import fileform
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def uhome(request):
    return render(request,'register.html')
def home(request):
    return render(request,'homepage.html')
def register(request): # need to create the function
    if request.method=="POST":
        passwor=request.POST['password']
        cpasswor=request.POST['cpassword']
        email=request.POST['email']
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        dob=request.POST['dob']
        phone=request.POST['phone']
        healthissue=request.POST['healthissue']
        interest=request.POST['interest']
        context=Registeration.objects.all().filter(email=email).exists()
        if(context==False):
            if(cpasswor==passwor):
                s=Registeration(password=passwor,email=email)
                s.save()
                r=userprofile(firstname=firstname,lastname=lastname,dob=dob,phone=phone,healthissue=healthissue,interest=interest,email=email)
                r.save()
                return render(request,'login.html')
            else:
                messages.error(request,"password and confirm password are not same!!!")
                return render(request,'register.html')
        else:
            return HttpResponse("Invalid form")
            
   
def login(request):
    if request.method == "POST":
        request.session['email']=request.POST['email']
        password=request.POST['password']
        if Registeration.objects.filter(email=request.session['email'], password=password).exists():
            log=Registeration.objects.get(email=request.session['email'], password=password)
            return render(request,'userhome.html')
        else:
           messages.error(request,"Wrong Password Please try again later!!!")
           return render(request,"login.html")
    else:
        return render(request,'login.html')
def uuhome(request):
    return render(request,'userhome.html')


def signin(request): # default page
    return render(request,'login.html')
def profile(request): # default page
    return render(request,'profile.html')
def addprofile(request): # need to create the function
    if request.method=="POST":
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        dob=request.POST['dob']
        phone=request.POST['phone']
        healthissue=request.POST['healthissue']
        interest=request.POST['interest']
        hobby=request.POST['hobby']
        economic_pref=request.POST['economic_pref']
        email=request.session['email']
        s=userprofile(firstname=firstname,lastname=lastname,dob=dob,phone=phone,healthissue=healthissue,interest=interest,hobby=hobby,economic_pref=economic_pref,email=email)
        s.save()
        return HttpResponse("Added successfully")
        
def viewprofile(request):
        email=request.session['email']
        profile={'userprofile':userprofile.objects.all().filter(email=email)}
        return render(request,'profile_list.html',profile)   

def recordupdate(request,id):
    recor={'rec':myrecord.objects.filter(pk=id)}
    return render(request,'updaterecord.html',recor)                   

def updateprofile(request):
    profile={'userprofile':userprofile.objects.all().filter(email=request.session['email'])}
    return render(request,'updateprofile.html',profile)

def updated(request):
    name=request.POST['name']
    lastname=request.POST['lname']
    dob=request.POST['dob']
    phone=request.POST['phone']
    healthissue=request.POST['healthissue']
    interest=request.POST['interest']
    hobby=request.POST['hobby']
    economic_pref=request.POST['economic_pref']
    userprofile.objects.all().filter(email=request.session['email']).update(firstname=name,lastname=lastname,dob=dob,phone=phone,healthissue=healthissue,interest=interest,hobby=hobby,economic_pref=economic_pref)
    messages.success(request,"Updated successfully!!!")
    return redirect("/updateprofile")
    


def addrecord(request):
    if request.method=="POST":
        hospitalname=request.POST['hospitalname']
        doctorname=request.POST['doctorname']
        hospitallocation=request.POST['hospitallocation']
        diseasename=request.POST['diseasename']
        documentname=request.POST['documentname']
        prescription=request.FILES['prescription']
        file=request.FILES['file']
        description=request.POST['description']
        email=request.POST['email']
        myrecord.objects.create(email=email,hospitallocation=hospitallocation,hospitalname=hospitalname,doctorname=doctorname,diseasename=diseasename,documentname=documentname,prescription=prescription,file=file,description=description)
        messages.success(request,"Upload successfully!!!")
        return redirect("/rec")
    else:
        messages.error(request,"Please Try again!!!")
        return redirect("/rec")
            

def rec(request):
    context=Registeration.objects.all().filter(email=request.session['email'])
    return render(request,'myrecord.html',{'context':context})

    
def viewrecord(request):
        email=request.session['email']
        Record={'myrecord':myrecord.objects.all().filter(email=email)}
        return render(request,'viewrecord.html',Record)

def emergencydelete(request):
    return redirect('viewemergency.html')
def addprescription(request):
    if request.method=="POST":
        email=request.session['email']
        diseasename=request.POST['diseasename']
        time=request.POST['time']
        mealname=request.POST['meal']
        description=request.POST['description']
        prescript=request.POST['prescriptionname']
        #medicinename=request.POST['medicinename']
        s=prescription(diseasename=diseasename,time=time,meal=mealname,description=description,
        prescrip_name=prescript,email=email)
        s.save()
        messages.success(request,"Updated successfully!!!")
        return redirect("/pres/")
def pres(request):
    return render(request,'prescription.html')

def viewpres(request):
        email=request.session['email']
        Record={'prescription':prescription.objects.all().filter(email=email)}
        return render(request,'viewprescription.html',Record)

def addemer(request): # default page
    return render(request,'emergency.html')
def addemergency(request): # need to create the function
    if request.method=="POST":
        hospitalname=request.POST['hname']
        location=request.POST['location']    
        phone=request.POST['phone']
        special=request.POST['spl']
        s=emergency(hospitalname=hospitalname,location=location,phone=phone,speciality=special)
        s.save()
        messages.success(request,"Emergency details Updated successfully!!!")
        return redirect("/addemer/")
def viewemergency(request):
        emergencyview={'emergency':emergency.objects.all()}
        return render(request,'viewemergency.html',emergencyview)
def uviewemergency(request):
        emergencyview={'emergency':emergency.objects.all()}
        return render(request,'uviewemergency.html',emergencyview)
def adminlogin(request):
    if request.method == "POST":
        request.session['email']=request.POST['email']
        password=request.POST['password']
        if hadmin.objects.filter(email=request.session['email'], password=password).exists():
            log=hadmin.objects.get(email=request.session['email'], password=password)
            return render(request,'adminhome.html')
        else:
           return render(request,"Error.html")
    else:
        return render(request,'headlogin.html')
def emerdelete(request,id):
    emer=emergency.objects.get(pk=id)
    emer.delete()
    return redirect("/viewemergency")

def emerupdate(request,id):
    emergen={'emer':emergency.objects.filter(pk=id)}
    return render(request,'updateemergency.html',emergen)

def updateemergency(request): # need to create the function
    if request.method=="POST":
        id=request.POST['id']
        hospitalname=request.POST['hname']
        location=request.POST['location']    
        phone=request.POST['phone']
        spl=request.POST['spl']
        emergen={'emer':emergency.objects.get(pk=id)}
        s=emergency.objects.filter(id=id).update(hospitalname=hospitalname,location=location,phone=phone,speciality=spl)
        messages.success(request,"Updated successfully!!!")
        return redirect("/viewemergency/")
        

def recordupdate(request,id):
    recor={'rec':myrecord.objects.filter(pk=id)}
    
    return render(request,'updaterecord.html',recor)

def presupdate(request,id): # need to create the function
    presc={'pres':prescription.objects.filter(pk=id)}
    return render(request,'updatepres.html',presc)


def recordelete(request,id):
    recor=myrecord.objects.get(pk=id)
    recor.delete()
    return redirect("/viewrecord")

def presdelete(request,id):
    pres=prescription.objects.get(pk=id)
    pres.delete()
    return redirect("/viewpres")


def updateprescription(request):
    if request.method=="POST":
        id=request.POST['id']
        email=request.session['email']
        diseasename=request.POST['diseasename']
        time=request.POST['time']
        mealname=request.POST['meal']
        description=request.POST['description']
        prescript=request.POST['prescriptionname']
        #medicinename=request.POST['medicinename']
        recor={'rec':prescription.objects.get(pk=id)}
        s=prescription.objects.filter(id=id).update(diseasename=diseasename,time=time,meal=mealname,description=description,
        prescrip_name=prescript,email=email)
        messages.success(request,"Updated successfully!!!")
        return redirect("/viewpres/")
def updaterecord(request): # need to create the function
    if request.method=="POST":
        id=request.POST['id']
        hospitalname=request.POST['hname']
        doctorname=request.POST['dname']
        hospitallocation=request.POST['hlocation']
        diseasename=request.POST['diname']
        date=request.POST['date']
        documentname=request.POST['dtname']
        description=request.POST['desc']
        prescription=request.POST['presc']
        file=request.POST['fil']
        email=request.session['email']
        presc={'pres':myrecord.objects.get(pk=id)}
        s=myrecord.objects.filter(id=id).update(hospitalname=hospitalname,doctorname=doctorname,hospitallocation=hospitallocation,diseasename=diseasename,date=date,
        documentname=documentname,description=description,prescription=prescription,file=file,email=email)
        messages.success(request,"Updated successfully!!!")
        return redirect("/viewrecord/")
    
def searchhos(request):
        email=request.session['email']
        Record={'myrecord':myrecord.objects.all().filter(email=email).distinct('hospitalname')}
        return render(request,'search.html',Record)

def shos(request):
        hos=request.POST['hospital']
        email=request.session['email']
        Record={'myrecord':myrecord.objects.all().filter(email=email,hospitalname=hos)}
        return render(request,'views.html',Record)


def searchdoc(request):
        email=request.session['email']
        Record={'myrecord':myrecord.objects.all().filter(email=email).distinct('doctorname')}
        return render(request,'searchdoc.html',Record)

def sdoc(request):
        doctor=request.POST['doctor']
        email=request.session['email']
        Record={'myrecord':myrecord.objects.all().filter(email=email,doctorname=doctor)}
        return render(request,'views.html',Record)



def searchdocname(request):
        email=request.session['email']
        Record={'myrecord':myrecord.objects.all().filter(email=email)}
        return render(request,'searchdocname.html',Record)

def sdocname(request):
        document=request.POST['document']
        email=request.session['email']
        Record={'myrecord':myrecord.objects.all().filter(email=email,documentname=document)}
        return render(request,'views.html',Record)

def searchemerloc(request):
        emergenc={'emergency':emergency.objects.all().distinct('location')}
        return render(request,'searchemerloc.html',emergenc)

def semerloc(request):
        loc=request.POST['ehloc']
        Record={'emergency':emergency.objects.all().filter(location=loc)}
        return render(request,'uviewemergency.html',Record)



def searchemerhname(request):
        emergenc={'emergency':emergency.objects.all().distinct('hospitalname')}
        return render(request,'searchemername.html',emergenc)

def semerhname(request):
        hname=request.POST['ehname']
        Record={'emergency':emergency.objects.all().filter(hospitalname=hname)}
        return render(request,'uviewemergency.html',Record)



def searchspl(request):
        emergenc={'emergency':emergency.objects.all().distinct('speciality')}
        return render(request,'searchspl.html',emergenc)

def semerspl(request):
        splname=request.POST['espl']
        Record={'emergency':emergency.objects.all().filter(speciality=splname)}
        return render(request,'uviewemergency.html',Record)


def logout(request):
    try:
         del request.session['email']
    except:
         return render(request,'homepage.html')
    return render(request,'homepage.html')

def about(request):
    return render(request,'about.html')

def ahome(request):
        return render(request,'adminhome.html')


def changepassword(request):
    return render(request,'changepassword.html')

def forgotpasssent(request):
        if request.method == 'POST':
            mail=request.POST['email']
            request.session['email']=request.POST['email']
            context=Registeration.objects.filter(email=mail).exists()
            if(context==True):
                send_mail(
                    subject='Click the link to get redirected to ',
                    message = 'http://127.0.0.1:8000/changepassword/',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[request.POST['email']],
                    fail_silently=False
                )
                messages.success(request,"Recovery Email has been sent to your Emai ID")
                return redirect("/forgotpassword/")
            else:
                messages.error(request,"Sorry! It is not a registered Email Id")
                return redirect("/forgotpassword/")
        else:
            return HttpResponse('NO')

def changedpassword(request):
    if request.method == "POST":
        new=request.POST['new']   
        email=request.session['email'] 
        Registeration.objects.filter(email=request.session['email']).update(password=new)
        return redirect('/login/')
def forgotpass(request):
    return render(request,'base1.html')

def cp(request):
     return render(request,'cp.html')
