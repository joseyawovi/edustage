from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Course, Registration
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from django.db import transaction
from django.utils import timezone
from datetime import datetime
import pytz

#home view
def home(request):
    courses = Course.objects.all()
    return render(request, 'classes/index.html', {'courses': courses})

#course detail view
def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug) 
    now = timezone.now()
    local_tz = pytz.timezone('Asia/Kolkata') 
    local_now = now.astimezone(local_tz)
    course_start_datetime = datetime.combine(course.start_date, course.start_time).astimezone(local_tz)
    course_end_datetime = datetime.combine(course.end_date, course.end_time).astimezone(local_tz) if course.end_date and course.end_time else None
    is_registered = False
    if request.user.is_authenticated:
        is_registered = Registration.objects.filter(user=request.user, course=course).exists()
    context = {
        'course': course,
        'now': local_now,
        'is_registered': is_registered,
        'course_start_datetime': course_start_datetime,
        'course_end_datetime': course_end_datetime,
    }
    return render(request, 'classes/class_detail.html', context)

# courses view
def courses(request):
    courses = Course.objects.all()
    
    return render(request,"classes/courses.html",{'courses': courses})

def join_course(request, slug):
    selected_course = Course.objects.get(slug=slug)
    return redirect(selected_course.google_meet_link)

@login_required
def register_course(request, slug):
    try:
        course = Course.objects.get(slug=slug)
    except Course.DoesNotExist:
        return HttpResponseNotFound("Course not found.")

    # Check for existing registration
    if Registration.objects.filter(course=course, user=request.user).exists():
        messages.error(request, "You are already registered for this course.")
        return redirect('course_detail', slug=slug)  # Assuming you have this URL name for the course detail page.

    # Start a transaction to ensure data integrity
    with transaction.atomic():
        new_registration = Registration(course=course, user=request.user)
        new_registration.save()

        # Send confirmation email
        try:
           send_mail(
    subject='Confirmation de votre inscription à la classe',
    message=f'''
Bonjour {request.user.first_name},

Félicitations et bienvenue à la formation {new_registration.course.title} ! Nous sommes ravis de vous compter parmi nous et nous sommes convaincus que vous ferez des progrès remarquables dans ce domaine passionnant.

Pour rester informé et connecter avec les autres participants, nous vous invitons à rejoindre le groupe WhatsApp officiel de NeoFormation. Cliquez simplement sur ce lien pour rejoindre : [Groupe WhatsApp NeoFormation](https://chat.whatsapp.com/HxXZgzTu730CYVvz8d0uO0)

### Détails du cours :
- **Nom du cours** : {new_registration.course.title}
- **Date de début** : {new_registration.course.start_date.strftime('%d %B %Y')}
- **Heure** : {new_registration.course.start_time.strftime('%H:%M')} UTC

Nous restons à votre disposition pour toute question. Préparez-vous à une expérience d'apprentissage enrichissante et dynamique !

Cordialement,

L'équipe NeoFormation
''',
    from_email=settings.DEFAULT_FROM_EMAIL,
    recipient_list=[request.user.email],
    html_message=f'''
<p>Bonjour {request.user.first_name},</p>

<p>Félicitations et bienvenue à la formation <strong>{new_registration.course.title}</strong> ! Nous sommes ravis de vous compter parmi nous et nous sommes convaincus que vous ferez des progrès remarquables dans ce domaine passionnant.</p>

<p>Pour rester informé et connecter avec les autres participants, nous vous invitons à rejoindre le groupe WhatsApp officiel de NeoFormation. Cliquez simplement sur ce lien pour rejoindre : <a href="https://chat.whatsapp.com/HxXZgzTu730CYVvz8d0uO0">Groupe WhatsApp NeoFormation</a></p>

<h3>Détails du cours :</h3>
<ul>
    <li><strong>Nom du cours</strong> : {new_registration.course.title}</li>
    <li><strong>Date de début</strong> : {new_registration.course.start_date.strftime('%d %B %Y')}</li>
    <li><strong>Heure</strong> : {new_registration.course.start_time.strftime('%H:%M')} UTC</li>
</ul>

<p>Nous restons à votre disposition pour toute question. Préparez-vous à une expérience d'apprentissage enrichissante et dynamique !</p>

<p>Cordialement,</p>
<p>L'équipe NeoFormation</p>
''',
)

        except Exception as e:
            messages.warning(request, "Registration successful but email could not be sent.")
            return redirect('course_detail', slug=slug)

    # Success
    messages.success(request, "You've successfully registered for the course!")
    return redirect('course_detail', slug=slug)


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
