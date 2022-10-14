from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone')
        addr = request.POST.get('address')

        UserModel.objects.create_user(username=username,password=password,phone_number=phone_number,addr=addr)

        print(UserModel.objects.all)

        return redirect('/login')

def signin(request):
    if request.method == 'GET':
        return render(request,'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        my_user = auth.authenticate(request,username=username,password=password)
        if my_user is not None:
            auth.login(request,my_user)
            return redirect('/home')
        else:
            return redirect('/login')