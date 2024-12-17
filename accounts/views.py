from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from .models import Faculty,Institution


# Create your views here.
def home(request):
    return render(request, 'Accounts/home.html')

def login(request):
    return render(request, 'Accounts/login.html')

def facultylogin(request):
    if request.method == 'POST':
        # Get the submitted username and password from the form
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user with the provided credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If the user is authenticated, log them in
            login(request, user)

            # Redirect to the faculty dashboard (ensure the URL name matches)
            return redirect('facultydashboard')  # Adjust the URL name to match your configuration
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password')
            return redirect('facultylogin')
    return render(request, 'Accounts/facultylogin.html')

def signup(request):
    return render(request, 'Accounts/signup.html')

def facultysignup(request):
    if request.method == "POST":
        institution_name = request.POST.get('institutionname')
        institution_id = request.POST.get('institutionid')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phonenumber')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('facultysignup')

        # Check if institution already exists or create a new one
        institution, created = Institution.objects.get_or_create(
            institution_id=institution_id,
            defaults={'name': institution_name}
        )

        # Check if the username already exists in Faculty model
        if Faculty.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('facultysignup')

        # Create the faculty object and save it
        faculty = Faculty(
            username=username,
            email=email,
            phone_number=phone_number,
            institution=institution,
            password=make_password(password1)  # Ensure password is hashed
        )
        faculty.save()

        messages.success(request, "Faculty created successfully! You can now log in.")
        return redirect('facultylogin')  # Redirect to faculty login page

    return render(request, 'accounts/facultysignup.html')

def forgotpassword(request):
    return render(request, 'Accounts/forgotpassword.html')
