from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


# Home view
def home(request):

    records = Record.objects.all()

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
    return render(request, 'home.html', {'records': records})

# Logout view
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')

# Register view

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the new user
            messages.success(request, "Registration successful!")
            return redirect('home')  # Redirect to a page (e.g., home)
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})




def customer_record(request, pk):
    if request.user.is_authenticated:
        # Lookup the record
        customer_record = get_object_or_404(Record, id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You must be logged in to view that page.")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        # Use get_object_or_404 directly
        delete_it = get_object_or_404(Record, id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully.")
        return redirect('home')
    else:
        messages.error(request, "You must be logged in to perform this action.")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "record Added....")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "you must be logged in to add")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record= get_object_or_404(Record, id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated")
            return redirect('home')
        return render(request, 'update_record.html',{'form':form} )
    else:
        messages.success(request, 'you must be logged in ')
        return redirect('home')
