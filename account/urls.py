# account/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('my_courses/', views.my_courses, name='my_courses'),  # Add this line
    path('change-password/', views.change_password, name='change_password'),
    path('logout/', views.logout_view, name='logout')
]

urlpatterns += [
    # ... other URL patterns
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
