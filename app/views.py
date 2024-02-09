from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def projects(request):
    return render(request, 'projects.html')
def blog(request): 
    return render(request, 'blog.html')
def contact(request): 
    return render(request, 'contact.html')
def projects(request): 
    return render(request, 'projects.html')
def purchase(request):
    return render(request, 'purchase.html')
def timeline(request): 
    return render(request, 'timeline.html')
def arcade(request): 
    return render(request, 'arcade.html')
def payment(request): 
    return render(request, 'payment.html')
def tetris(request): 
    return render(request, 'tetris.html')
def snake(request): 
    return render(request, 'snake.html')
def password(request): 
    return render(request, 'password.html')
def pong(request): 
    return render(request, 'pong.html')
def signup(request): 
    return render(request, 'signup.html')
def mario(request): 
    return render(request, 'mario.html')
def login(request): 
    return render(request, 'login.html')
def forgetpass(request): 
    return render(request, 'forgetpass.html')
def blogmenu(request): 
    return render(request, 'blogmenu.html')
def verification(request): 
    return render(request, 'verification.html')
def notepad(request): 
    return render(request, 'notepad.html')
def myip(request): 
    return render(request, 'myip.html')
def calculator(request): 
    return render(request, 'calculator.html')
def arcadegames(request): 
    return render(request, 'arcadegames.html')
def profile(request): 
    return render(request, 'profile.html')
def camera(request): 
    return render(request, 'camera.html')
def internetspeedtest(request): 
    return render(request, 'internetspeedtest.html')
def resetpassword(request): 
    return render(request, 'resetpassword.html')
def tools(request): 
    return render(request, 'tools.html')
def passwordgenerator(request): 
    return render(request, 'passwordgenerator.html')
def settings(request): 
    return render(request, 'settings.html')
def home(request):
    return redirect('/')

#function for register 

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordre = request.POST.get('passwordre')
        
        # Check if any of the fields are empty
        if not (username and email and password and passwordre):
            messages.info(request, "Please provide all needed information.")
            return redirect('signup')
        
        # Check password length
        if len(password) < 6 or len(passwordre) < 6:
            messages.info(request, "Your password must be at least 6 characters.")
            return redirect('signup')
        
        # Check if passwords match
        if password != passwordre:
            messages.info(request, "Passwords do not match.")
            return redirect('signup')
        
        # Check for existing email and username
        if User.objects.filter(email=email).exists():
            messages.info(request, "Email Already Used")
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.info(request, "Username Already Used")
            return redirect('signup')
        
        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'signup.html')
    
#function for login

def login(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if both username and password are empty
        if not username and not password:
            messages.info(request, 'Please provide a username and password')
            return redirect('login')
        
        # Check if the username exists
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.info(request, 'Username is incorrect')
            return redirect('login')

        # Check if the password is correct for the given username
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Password is incorrect')
            return redirect('login')
    else:
        return render(request, 'login.html')
# function for logout

def logout(request):
    auth.logout(request)
    return redirect('/')




#mrnone wrote this 