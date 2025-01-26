from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Home view
def home(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in successfully.") 
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in. Please try again.")
    
    # Render the home page
    return render(request, 'home.html', {})

# Logout view
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')

# Register view
def register_user(request):
    return render(request, 'register.html', {})
