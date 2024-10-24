from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_list, name='home'),  # Home page that lists all classes
    path('courses', views.course_list, name="course_list"),
    path('join_course/<slug:slug>/', views.join_course, name='join_course'),
    path('register_course/<slug:slug>/', views.register_course, name='register_course'),
    path('detail/<slug:slug>/', views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/like/', views.toggle_like, name='toggle_like'),
]
