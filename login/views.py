from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from django.contrib import messages
from .models import Users
import datetime
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse
from textblob import TextBlob



# Create your views here.

def home(request):
    x = datetime.date.today()
    return render(request,'home.html',{"time":x})


def reg(request):
    return render(request,'registration.html')


def login(request):
    return render(request,'login.html')

def success(request):
    return render(request,'success.html')



def registration(request):

    if(request.method=="POST"):
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if(password==password_confirmation):
            user = Users.objects.filter(mail=email).count()
            if(user):
                messages.info(request,"Email id already exists !")
                return render(request,'registration.html')

            else:
                password = make_password(password)
                user=Users(name=name,mobile=mobile,mail=email,password=password)
                user.save()
                return render(request,'success.html')
                
            

        else:
            messages.info(request,"Password not same !")
            return render(request,'registration.html')

    else:
        messages.info(request,"Method is not POST !")
        return render(request,'registration.html')





def login_auth(request):
    if(request.method=="POST"):
        email = request.POST['mail']
        user = Users.objects.filter(mail=email).count()
        if(user):
            user =  Users.objects.get(mail=email)
            password = request.POST['password']

            if(check_password(password,user.password)):
                request.session['user']=user.id
                return redirect('/dashboard')
                

            else:
                messages.info(request,"Invalid user id or password !")
                return render(request,'login.html')

        else:
            messages.info(request,"Invalid user id or password !")
            return render(request,'login.html')



def dashboard(request):
    if(request.session.get('user')):
        user = Users.objects.filter(id=request.session['user']).count()
        if(user):
            user =  Users.objects.get(id=request.session['user'])
            return render(request,'dashboard.html',{'name':user.name,'email':user.mail,'mobile':user.mobile})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    request.session.clear()
    return redirect('/login')




def ajax_call(request):         # sentiment

    if request.method=="POST":
        return JsonResponse({"value":TextBlob(request.POST['text']).sentiment.polarity},status=200)



def profile_change(request):

    if(request.session.get('user')):
        user = Users.objects.filter(id=request.session['user']).count()
        if(user):
            user =  Users.objects.get(id=request.session['user'])
            return render(request,'profile_change.html',{'name':user.name,'email':user.mail,'mobile':user.mobile})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def profile_change_form(request):
    if(request.method=="POST"):
        email = request.POST['mail']
        user = Users.objects.get(mail=email)

        user.name = request.POST['name']
        user.mobile = request.POST['mobile']

        if(request.POST['password']!=""):
            user.password = make_password(request.POST['password'])
        user.save()
    return redirect("/dashboard")


def text_check(request):
    return render(request,"text_process.html")