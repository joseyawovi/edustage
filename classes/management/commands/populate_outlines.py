from django.core.management.base import BaseCommand
from ...models import Course, Outline, SubOutline

class Command(BaseCommand):
    help = 'Populate the Django BootCamp course with outlines and sub-outlines'

    def handle(self, *args, **kwargs):
        try:
            django_bootcamp = Course.objects.get(title='Django BootCamp')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR("The course 'Django Bootcamp' does not exist. Please create the course first."))
        else:
            outline_titles = [
                'Introduction to Django', 
                'Django Models and ORM', 
                'Views and Templates', 
                'Django Forms', 
                'Authentication and Authorization',
                'Deployment'
            ]

            sub_outline_titles = [
                ['Installing Django', 'Project Setup', 'Django Settings'],
                ['Creating Models', 'Migrations', 'Querying the Database'],
                ['Rendering Templates', 'Django Views', 'Template Inheritance'],
                ['Creating Forms', 'Handling Form Submissions', 'Form Validation'],
                ['User Authentication', 'User Authorization', 'Password Management'],
                ['Preparing for Deployment', 'Deploying on Heroku', 'Managing Static Files']
            ]

            for i, outline_title in enumerate(outline_titles):
                outline, created = Outline.objects.get_or_create(
                    course=django_bootcamp,
                    title=outline_title,
                    description=f"This is the outline for {outline_title} in the Django Bootcamp course."
                )

                for sub_outline_title in sub_outline_titles[i]:
                    SubOutline.objects.get_or_create(
                        course_outline=outline,
                        sub_title=sub_outline_title
                    )

            self.stdout.write(self.style.SUCCESS("Successfully populated outlines and sub-outlines for Django Bootcamp."))
