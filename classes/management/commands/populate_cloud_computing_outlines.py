from django.core.management.base import BaseCommand
from ...models import Course, Outline, SubOutline  # Update with the correct model path

class Command(BaseCommand):
    help = 'Populate the Cloud Computing BootCamp course with outlines and sub-outlines'

    def handle(self, *args, **kwargs):
        try:
            cloud_computing_bootcamp = Course.objects.get(title='Cloud Computing')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR("The course 'Cloud Computing BootCamp' does not exist. Please create the course first."))
        else:
            outline_titles = [
                'Introduction to Cloud Computing', 
                'Cloud Service Models', 
                'Cloud Deployment Models',
                'Security in Cloud Computing', 
                'Cloud Architecture', 
                'Future Trends in Cloud Computing'
            ]

            sub_outline_titles = [
                ['What is Cloud Computing?', 'History of Cloud Computing', 'Benefits of Cloud Computing'],
                ['Infrastructure as a Service (IaaS)', 'Platform as a Service (PaaS)', 'Software as a Service (SaaS)'],
                ['Public Cloud', 'Private Cloud', 'Hybrid Cloud'],
                ['Common Security Risks', 'Best Practices for Security', 'Compliance in the Cloud'],
                ['Components of Cloud Architecture', 'Designing Cloud Solutions', 'Cloud Management'],
                ['Emerging Technologies', 'Impact of AI on Cloud Computing', 'Trends and Predictions']
            ]

            for i, outline_title in enumerate(outline_titles):
                outline, created = Outline.objects.get_or_create(
                    course=cloud_computing_bootcamp,
                    title=outline_title,
                    description=f"This is the outline for {outline_title} in the Cloud Computing BootCamp course."
                )

                for sub_outline_title in sub_outline_titles[i]:
                    SubOutline.objects.get_or_create(
                        course_outline=outline,
                        sub_title=sub_outline_title
                    )

            self.stdout.write(self.style.SUCCESS("Successfully populated outlines and sub-outlines for Cloud Computing BootCamp."))
