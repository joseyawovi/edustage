from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from classes.models import Registration

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Change to your dashboard URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Change to your dashboard URL
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_update')  # Change to your dashboard URL
    else:
        form = CustomUserUpdateForm(instance=request.user)
    return render(request, 'account/update_profile.html', {'form': form})


@login_required
def my_courses(request):
    registrations = Registration.objects.filter(user = request.user)
    context ={
        "registrations":registrations
    }
    return render(request, 'account/my_course.html',context)  # You can create this template later


def logout_view(request):
    logout(request)  # Logs out the user associated with the request
    return redirect('home')  # Redirects to the 'home' page (replace 'home' with your URL name)


