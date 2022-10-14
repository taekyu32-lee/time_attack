from django.shortcuts import render, redirect
from .models import UserModel

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

        return redirect('/signin')

def signin(request):
    if request.method == 'GET':
        return render(request,'login.html')