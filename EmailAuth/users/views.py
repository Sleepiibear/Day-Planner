from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            email = request.POST['email']
            try:
                print("catching error")
                username = User.objects.get(email=email.lower()).username
            except:
                print("error detected")
                return render(request, 'login.html', {'error':'Not a Valid Email Address'})
            print("here we go")
            user = auth.authenticate(username = username, password = request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error':'Not a Valid Email Address'})
        else:
            return render(request, 'login.html')
    else:
        return redirect('home')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')

def home(request):
    return render(request, 'home.html')

