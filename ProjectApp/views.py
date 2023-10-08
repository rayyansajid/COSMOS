from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def registration(request):
    if request.method=='POST':
        f_name = request.POST['fname']
        age = request.POST['age']
        phno = request.POST['phno']
        email = request.POST['email']
        username = request.POST['username']
        psw = request.POST['psw']
        
        user = User.objects.create_user(username=username, password=psw)
        login(request, user)
        print(f_name)
        return render(request, 'index.html')
    return render(request,'registration.html')

def homepage(request):
    return render(request, 'index.html')

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        psw = request.POST['psw']
        user = authenticate(username = username, password=psw)
        print(user)
        if user is not None:
            print("user is not none")
            logger.debug("Logged In, Successfully!")
            login(request, user)
            return redirect('homepage')
        print("user is none")
        logger.debug("Incorrect username and/or password.")
        return render(request, 'login.html')
    return render(request, 'login.html')
def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect('homepage')
def earth(request):
    return render(request, 'earth.html')

def mars(request):
    return render(request, 'mars.html')

def moon(request):
    return render(request, 'moon.html')

def ship(request):
    return render(request, 'Spaceship.html')

def station(request):
    return render(request, 'spacestation.html')