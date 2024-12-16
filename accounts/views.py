from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Accounts/home.html')

def login(request):
    return render(request, 'Accounts/login.html')

def signup(request):
    return render(request, 'Accounts/signup.html')

def forgotpassword(request):
    return render(request, 'Accounts/forgotpassword.html')
