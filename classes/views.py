from django.shortcuts import render, redirect
from .models import Course, Registration
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime
import pytz

def class_list(request):
    courses = Course.objects.all()
    return render(request, 'classes/index.html', {'courses': courses})

def course_list(request):
    courses = Course.objects.all()
    
    return render(request,"classes/course_list.html",{'courses': courses})

def course_detail(request, slug):
    course = Course.objects.get(slug=slug)
    
    # Get the current time in server's timezone and convert to local timezone
    now = timezone.now()
    local_tz = pytz.timezone('Asia/Kolkata')  # India Standard Time
    local_now = now.astimezone(local_tz)

    # Combine start and end datetime for comparison in local timezone
    course_start_datetime = datetime.combine(course.start_date, course.start_time).astimezone(local_tz)
    course_end_datetime = datetime.combine(course.end_date, course.end_time).astimezone(local_tz) if course.end_date and course.end_time else None

    if request.user.is_authenticated:
        is_registered = Registration.objects.filter(user=request.user, course=course).exists()

    context = {
        'course': course,
        'now': local_now,  # Now in local timezone
        'is_registered': is_registered,
        'course_start_datetime': course_start_datetime,
        'course_end_datetime': course_end_datetime,
    }

    return render(request, 'classes/class_detail.html', context)


def join_course(request, slug):
    selected_course = Course.objects.get(slug=slug)
    return redirect(selected_course.google_meet_link)

def register_course(request, slug):

    try:
        course = Course.objects.get(slug=slug)
    except Course.DoesNotExist:
        return HttpResponseNotFound("Course not found.")
    
    
    if not request.user.is_authenticated:
        raise PermissionError("You must be logged in to register for a course.")
    else:
        email = request.user.email

    # Check for existing registration (optional)
    if Registration.objects.filter(course=course, user=request.user).exists():
        return HttpResponse("You are already registered for this course.")

    new_registration = Registration(course=course, user=request.user)
    new_registration.save()
    send_mail(
            'Class Registration Confirmation',
            f'Thank you for registering for {new_registration.course.title}. Join here: {new_registration.course.google_meet_link}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
        )
    # Choose success message/redirect based on your application logic
    success_message = "You've successfully registered for the course!"
    # return HttpResponse(success_message)  # For a simple success message

    return redirect("my_courses")  # For redirecting to the dashboard



from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def toggle_like(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    liked = False
    if request.user in course.likes.all():
        course.likes.remove(request.user)  # Unlike
    else:
        course.likes.add(request.user)  # Like
        liked = True
    
    # Return the new like status and count as JSON
    return JsonResponse({
        'liked': liked,
        'likes_count': course.likes.count()
    })
