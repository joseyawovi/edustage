from django.core.management.base import BaseCommand
from ...models import Course, Outline, SubOutline  # Update with the correct model path

class Command(BaseCommand):
    help = 'Populate the Information Technology BootCamp course with outlines and sub-outlines'

    def handle(self, *args, **kwargs):
        try:
            it_bootcamp = Course.objects.get(title='Information Technology BootCamp')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR("The course 'Information Technology BootCamp' does not exist. Please create the course first."))
        else:
            outline_titles = [
                'Introduction to Information Technology', 
                'Networking Fundamentals', 
                'Database Management',
                'Software Development', 
                'IT Security', 
                'Emerging Technologies'
            ]

            sub_outline_titles = [
                ['What is Information Technology?', 'Key Concepts in IT', 'The Role of IT in Business'],
                ['Types of Networks', 'Network Topologies', 'Understanding the OSI Model'],
                ['Database Concepts', 'SQL vs. NoSQL', 'Database Design Principles'],
                ['Programming Basics', 'Software Development Life Cycle', 'Agile vs. Waterfall Methodologies'],
                ['Common Security Threats', 'Security Best Practices', 'Understanding Compliance and Regulations'],
                ['Cloud Computing', 'Artificial Intelligence', 'The Internet of Things (IoT)']
            ]

            for i, outline_title in enumerate(outline_titles):
                outline, created = Outline.objects.get_or_create(
                    course=it_bootcamp,
                    title=outline_title,
                    description=f"This is the outline for {outline_title} in the Information Technology BootCamp course."
                )

                for sub_outline_title in sub_outline_titles[i]:
                    SubOutline.objects.get_or_create(
                        course_outline=outline,
                        sub_title=sub_outline_title
                    )

            self.stdout.write(self.style.SUCCESS("Successfully populated outlines and sub-outlines for Information Technology BootCamp."))
