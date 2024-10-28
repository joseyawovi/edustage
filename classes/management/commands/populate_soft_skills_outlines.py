from django.core.management.base import BaseCommand
from ...models import Course, Outline, SubOutline  # Update with the correct model path

class Command(BaseCommand):
    help = 'Populate the Soft Skills BootCamp course with outlines and sub-outlines'

    def handle(self, *args, **kwargs):
        try:
            soft_skills_bootcamp = Course.objects.get(title='Soft Skills BootCamp')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR("The course 'Soft Skills BootCamp' does not exist. Please create the course first."))
        else:
            outline_titles = [
                'Introduction to Soft Skills', 
                'Communication Skills', 
                'Teamwork and Collaboration',
                'Problem-Solving Skills', 
                'Emotional Intelligence', 
                'Time Management'
            ]

            sub_outline_titles = [
                ['What are Soft Skills?', 'Importance of Soft Skills', 'Difference Between Hard Skills and Soft Skills'],
                ['Verbal Communication', 'Non-verbal Communication', 'Active Listening'],
                ['Building Trust', 'Conflict Resolution', 'Working in Diverse Teams'],
                ['Creative Thinking', 'Critical Thinking', 'Decision Making'],
                ['Understanding Emotions', 'Managing Emotions', 'Empathy in the Workplace'],
                ['Prioritization', 'Planning and Scheduling', 'Overcoming Procrastination']
            ]

            for i, outline_title in enumerate(outline_titles):
                outline, created = Outline.objects.get_or_create(
                    course=soft_skills_bootcamp,
                    title=outline_title,
                    description=f"This is the outline for {outline_title} in the Soft Skills BootCamp course."
                )

                for sub_outline_title in sub_outline_titles[i]:
                    SubOutline.objects.get_or_create(
                        course_outline=outline,
                        sub_title=sub_outline_title
                    )

            self.stdout.write(self.style.SUCCESS("Successfully populated outlines and sub-outlines for Soft Skills BootCamp."))
