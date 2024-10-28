from django.core.management.base import BaseCommand
from ...models import Course, Outline, SubOutline  # Update with the correct model path

class Command(BaseCommand):
    help = 'Populate the Digital Forensics BootCamp course with outlines and sub-outlines'

    def handle(self, *args, **kwargs):
        try:
            digital_forensics_bootcamp = Course.objects.get(title='Digital Forensics')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR("The course 'Digital Forensics' does not exist. Please create the course first."))
        else:
            outline_titles = [
                'Introduction to Digital Forensics', 
                'Types of Digital Forensics', 
                'Digital Evidence', 
                'Investigation Process', 
                'Tools and Techniques', 
                'Legal and Ethical Considerations'
            ]

            sub_outline_titles = [
                ['What is Digital Forensics?', 'History and Importance', 'Key Concepts in Digital Forensics'],
                ['Computer Forensics', 'Network Forensics', 'Mobile Device Forensics'],
                ['Types of Digital Evidence', 'Collecting Digital Evidence', 'Preserving Digital Evidence'],
                ['Stages of an Investigation', 'Evidence Collection', 'Reporting and Documentation'],
                ['Forensic Tools Overview', 'Data Recovery Techniques', 'Analyzing Digital Evidence'],
                ['Legal Framework', 'Ethics in Digital Forensics', 'Best Practices in Digital Investigations']
            ]

            for i, outline_title in enumerate(outline_titles):
                outline, created = Outline.objects.get_or_create(
                    course=digital_forensics_bootcamp,
                    title=outline_title,
                    description=f"This is the outline for {outline_title} in the Digital Forensics BootCamp course."
                )

                for sub_outline_title in sub_outline_titles[i]:
                    SubOutline.objects.get_or_create(
                        course_outline=outline,
                        sub_title=sub_outline_title
                    )

            self.stdout.write(self.style.SUCCESS("Successfully populated outlines and sub-outlines for Digital Forensics BootCamp."))
