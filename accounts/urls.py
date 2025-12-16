from django.urls import path
from .views import register, login_view, otp_verify, forgot_password, reset_otp, reset_password

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('otp/<str:email>/', otp_verify, name='otp'),

    path('forgot/', forgot_password, name='forgot'),
    path('reset-otp/<str:email>/', reset_otp, name='reset_otp'),
    path('reset-password/<str:email>/', reset_password, name='reset_password'),
]
