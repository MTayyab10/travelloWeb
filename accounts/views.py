from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "The Username has been taken already, Try another one!")
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request, "The email has been taken, try with another one")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name,
                                                last_name=last_name)

                user.save()
                print('User created')
                return redirect('login')
        else:
           print('Password not matched')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Username or Password!')
            return redirect('login')

    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')