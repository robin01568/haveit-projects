from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import *

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            pass1 = request.POST['password']
            pass2 = request.POST['password1']
            if pass1 == pass2:
                user = form.save(commit=False)
                user.set_password(pass1)
                user.is_customer = True
                form.save()

                return redirect('login')
        return redirect('register')
    form = RegisterForm()
    return render(request, 'userAccount/register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)

            return redirect('home')
    return render(request, 'userAccount/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_dashboard(request):
    return render(request, 'userAccount/profile/dashboard.html')


@login_required
def profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid or profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, 'User & Profile Updated sucesfully!!')
        else:
            messages.error(request, 'Somthing went Wrong!')

    user_form = UserUpdateForm(instance=user)
    profile_form = ProfileUpdateForm(instance=profile)
    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request, 'userAccount/profile/profile.html',context)


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
            return redirect('profile')