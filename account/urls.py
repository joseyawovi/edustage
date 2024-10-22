# account/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Add this line
]
