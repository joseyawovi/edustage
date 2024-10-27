from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm, EmailLoginForm,SignupForm
from django.contrib.auth import update_session_auth_hash
from classes.models import Registration
from django.contrib import messages


from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create the user
            user.backend = 'account.backends.EmailBackend'  # Set the backend
            print(f"User created: {user}")  # Debug: Check user object
            login(request, user)  # Log in the user
            print(f"User logged in: {request.user}")  # Debug: Check logged in user
            messages.success(request, "Signup successful!")
            return redirect('home')  # Redirect to the my_courses view
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)  # Using email for username
            if user is not None:
                login(request, user)
                return redirect('home')  # Change 'home' to your desired redirect URL
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = EmailLoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('my_courses')  # Redirect to a relevant page
    else:
        form = UpdateProfileForm(instance=user)
    
    return render(request, 'account/update_profile.html', {'form': form})

@login_required
def my_courses(request):
    registrations = Registration.objects.filter(user = request.user)
    context ={
        "registrations":registrations
    }
    return render(request, 'account/my_course.html',context)  # You can create this template later

from .forms import CustomPasswordChangeForm

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, "Your password was successfully updated!")
            return redirect('my_courses')  # Redirect to a relevant page
    else:
        form = CustomPasswordChangeForm(request.user)
    
    return render(request, 'account/change_password.html', {'form': form})

def logout_view(request):
    logout(request)  # Logs out the user associated with the request
    return redirect('home')  # Redirects to the 'home' page (replace 'home' with your URL name)


