from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import User_Detail
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('sign_up')
def sign_up(request):
    if request.method=='POST' and 'upload' in request.FILES:
        uname=request.POST['uname']
        password1=request.POST['password1']
        password2=request.POST['password2']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        lane=request.POST['lane']
        city=request.POST['city']
        state=request.POST['state']
        pin=request.POST['pin']
        usr=request.POST['usr']
        if usr==1:
            type="doctor"
        else:
            type="nurse"
        upload = request.FILES['upload']
        if password2!=password1:
             messages.warning(request, 'Password and confirm password does not match')
             return redirect('sign_up')
        user=User.objects.create_user(username=uname,password=password1)
        user.save()
        user_d=User_Detail(user=user,lane=lane,lname=lname,fname=fname,pic=upload,pin=pin,city=city,state=state,email=email,type=type)
        user_d.save()
        print('user created')
        auth.login(request,user)
        return redirect('home')
    else:
        return render(request,'sign_up.html')
def sign_in(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=uname,password=password)
        if user is None:
            return redirect('sign_up')
        if user is not None:
            auth.login(request,user)
            return redirect('home')
    else:
        return render(request,'sign_in.html')
def home(request):
        if request.user.is_authenticated:
            user=request.user
            objs =User_Detail.objects.filter(user=user)
            for x in objs:
                if x.type=="doctor":
                    return render(request,'index1.html',{'objs':objs})
                else:
                    return render(request,'index2.html',{'objs':objs})
        else:
            return redirect('sign_up')
