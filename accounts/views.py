from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import CustomUser
import random

from django.contrib.auth.hashers import make_password

OTP_STORE = {}

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        otp = random.randint(100000, 999999)
        OTP_STORE[user.email] = otp

        send_mail(
            'Email Verification OTP',
            f'Your OTP is {otp}',
            'admin@apexiums.com',
            [user.email]
        )
        return redirect('otp', email=user.email)
    return render(request, 'register.html', {'form': form})

def otp_verify(request, email):
    if request.method == 'POST':
        if int(request.POST['otp']) == OTP_STORE[email]:
            user = CustomUser.objects.get(email=email)
            user.is_active = True
            user.is_email_verified = True
            user.save()
            return redirect('login')
    return render(request, 'otp.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            email=request.POST['email'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')





FORGOT_OTP = {}

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = CustomUser.objects.filter(email=email).first()
        if user:
            otp = random.randint(100000, 999999)
            FORGOT_OTP[email] = otp

            send_mail(
                'Password Reset OTP',
                f'Your password reset OTP is {otp}',
                'admin@apexiums.com',
                [email]
            )
            return redirect('reset_otp', email=email)
    return render(request, 'forgot_password.html')


def reset_otp(request, email):
    if request.method == 'POST':
        if int(request.POST['otp']) == FORGOT_OTP[email]:
            return redirect('reset_password', email=email)
    return render(request, 'reset_otp.html')


def reset_password(request, email):
    if request.method == 'POST':
        password = request.POST['password']
        user = CustomUser.objects.get(email=email)
        user.password = make_password(password)
        user.save()
        return redirect('login')
    return render(request, 'reset_password.html')
