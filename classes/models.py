from django.db import models
from django.utils.text import slugify
from account.models import CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    google_meet_link = models.URLField(max_length=500)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    image = models.ImageField(upload_to='class_pictures/', null=True, blank=True)  # Class picture
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    lecturer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='lectured_courses')
    likes = models.ManyToManyField(User, related_name='liked_courses', blank=True)  # To track likes
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)  # New slug field

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
     # Method to count enrollments
    @property
    def enrollments(self):
        return Registration.objects.filter(course=self).count()

    # Method to count likes
    @property
    def likes_count(self):
        return self.likes.count()


class Outline(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='outlines')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} for {self.course.title}"
    
# SubOutline model (Sub-outlines for each course outline)
class SubOutline(models.Model):
    course_outline = models.ForeignKey(Outline, on_delete=models.CASCADE, related_name='sub_outlines')
    sub_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.course_outline.title} - {self.sub_title}"
    

class Registration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.course} - {self.user}"