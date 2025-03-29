from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import SignupForm
from .models import CustomUser,UserTypes,Donor,Organization

def home(request):
    return render(request,'home.html')

def signupDonor(request):
    form = None
    user_type =UserTypes.objects.filter(name="Donor").first()
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        pin = request.POST.get("pincode")
        phone = request.POST.get('phone')
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        profile_picture = request.FILES.get("profile_picture")
        
        if password1 != password2:
            messages.error(request,"Passwords didn't match")
            redirect('auth_signup_donor')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request,'Account with same username is already exists')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
        
            return redirect("auth_signup_donor")
        user = CustomUser(
            username = username,
            email = email,
            password = password1,
            profile_picture = profile_picture,
            phone_number = phone,
            user_type = user_type,
        )
        user.set_password(password1)    
        user.save()
        messages.success(request,"New Account is created for you")
        donor = Donor(
            user = user,
            address = address,
            pincode = pin
        )
        print(username,email,address,pin,phone,password1,password2)
        donor.save()
        user = authenticate(request=request,username=username,password=password1)
        messages.success(request,"You are authenticated..")
        messages.success(request,"Redirectiing to donor dashboard")
        if user is not None:
            login(request,user)
    return render(request, 'authenticate/signupDonor.html', {'form': form})



def signupOrganization(request):
    form = None
    user_type = UserTypes.objects.filter(name="Organization").first()
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        pin = request.POST.get("pincode")
        phone = request.POST.get('phone')
        license = request.POST.get('license')
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        profile_picture = request.FILES.get("profile_picture")
        
        if password1 != password2:
            messages.error(request,"Passwords didn't match")
            redirect('auth_signup_organization')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request,'Account with same username is already exists')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect("auth_signup_organization")
        user = CustomUser(
            username = username,
            email = email,
            password = password1,
            profile_picture = profile_picture,
            phone_number = phone,
            user_type = user_type,
        )
        user.set_password(password1)    
        user.save()
        messages.success(request,"New Account is created for you")
        donor = Organization(
            user = user,
            address = address,
            pincode = pin,
            license = license
        )
        print(username,email,address,pin,phone,password1,password2,license)
        donor.save()
        user = authenticate(request=request,username=username,password=password1)
        messages.success(request,"You are authenticated..")
        messages.success(request,"Redirectiing to donor dashboard")
        if user is not None:
            login(request,user)
    return render(request, 'authenticate/signupOrgnanization.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        user = authenticate(request=request,username=username,password=password)
        print(username,password,user,remember)
        if user is None :
            messages.error(request,'invalid username or password')
            return redirect('auth_login')
        messages.success(request,"Authenticated successfully")
        if remember:
            login(request,user)
    return render(request,'authenticate/login.html')


def user_logout(request):
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)  # Logs out the user before setting the message
        messages.success(request, f"{username} has been logged out successfully!")
    else:
        messages.warning(request, "You are not signed in!")
    return redirect("home")

# Create your views here.
