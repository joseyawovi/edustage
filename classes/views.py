from django.shortcuts import render, redirect
from .models import Course, Registration
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def class_list(request):
    courses = Course.objects.all()
    return render(request, 'classes/index.html', {'courses': courses})

def course_list(request):
    courses = Course.objects.all()
    
    return render(request,"classes/course_list.html",{'courses': courses})

def register_for_class(request, slug):
    selected_course = Course.objects.get(slug=slug)
    if request.method == 'POST':
        email = request.POST.get('email')
        # Send confirmation email (optional)
        send_mail(
            'Class Registration Confirmation',
            f'Thank you for registering for {selected_course.title}. Join here: {selected_course.google_meet_link}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
        )
        # Redirect user to Google Meet link
        return redirect(selected_course.google_meet_link)
    
    return render(request, 'classes/class_detail.html', {'course': selected_course})

def course_detail(request,slug):
    course = Course.objects.prefetch_related('outlines__sub_outlines').get(slug=slug)
    
    return render(request, 'classes/course_detail.html', {'course': course})

def register_course(request, slug):
    """Registers a user for a course.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The unique slug identifier for the course.

    Returns:
        HttpResponse: A response object indicating success or failure.

    Raises:
        Http404: If the course with the provided slug is not found.
        PermissionError: If the user is not authenticated.
    """

    try:
        course = Course.objects.get(slug=slug)
    except Course.DoesNotExist:
        return HttpResponseNotFound("Course not found.")

    if not request.user.is_authenticated:
        raise PermissionError("You must be logged in to register for a course.")

    # Check for existing registration (optional)
    if Registration.objects.filter(course=course, user=request.user).exists():
        return HttpResponse("You are already registered for this course.")

    new_registration = Registration(course=course, user=request.user)
    new_registration.save()

    # Choose success message/redirect based on your application logic
    success_message = "You've successfully registered for the course!"
    # return HttpResponse(success_message)  # For a simple success message

    return redirect("dashboard")  # For redirecting to the dashboard



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
