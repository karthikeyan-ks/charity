from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import SignupForm

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_verified = False  # Default value
            user.save()
            login(request, user)  # Automatically log in the user after signup
            return redirect('home')  # Redirect to the homepage or dashboard
    else:
        form = SignupForm()
    return render(request, 'authenticate/signup.html', {'form': form})

def login(request):
    return render(request,'authenticate/login.html')

# Create your views here.
