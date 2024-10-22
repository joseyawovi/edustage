from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_list, name='home'),  # Home page that lists all classes
    path('courses', views.course_list, name="course_list"),
    path('register/<slug:slug>/', views.register_for_class, name='register_for_class'),
    path('register_course/<slug:slug>/', views.register_course, name='register_course'),
    path('courses/<int:course_id>/like/', views.toggle_like, name='toggle_like'),
]
