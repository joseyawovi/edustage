# account/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('my_courses/', views.my_courses, name='my_courses'),  # Add this line
    path('logout/', views.logout_view, name='logout')
]
