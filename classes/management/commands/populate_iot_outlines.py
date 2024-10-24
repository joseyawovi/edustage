from django.core.management.base import BaseCommand
from ...models import Course, Outline, SubOutline  # Update with the correct model path

class Command(BaseCommand):
    help = 'Populate the Internet of Things BootCamp course with outlines and sub-outlines'

    def handle(self, *args, **kwargs):
        try:
            iot_bootcamp = Course.objects.get(title='Internet of Things')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR("The course 'Internet of Things' does not exist. Please create the course first."))
        else:
            outline_titles = [
                'Introduction to the Internet of Things', 
                'IoT Architecture and Components', 
                'IoT Communication Protocols',
                'Data Management in IoT', 
                'IoT Security', 
                'Future Trends in IoT'
            ]

            sub_outline_titles = [
                ['What is IoT?', 'History of IoT', 'Applications of IoT in Various Industries'],
                ['Key Components of IoT Systems', 'IoT Devices and Sensors', 'IoT Network Architecture'],
                ['Communication Protocols Overview', 'MQTT vs. HTTP', 'CoAP and Other Protocols'],
                ['Data Collection and Storage', 'Data Processing and Analysis', 'Cloud Computing in IoT'],
                ['Security Challenges in IoT', 'Best Practices for IoT Security', 'Regulations and Compliance'],
                ['Emerging Trends', 'IoT and Artificial Intelligence', 'Smart Cities and Smart Homes']
            ]

            for i, outline_title in enumerate(outline_titles):
                outline, created = Outline.objects.get_or_create(
                    course=iot_bootcamp,
                    title=outline_title,
                    description=f"This is the outline for {outline_title} in the Internet of Things BootCamp course."
                )

                for sub_outline_title in sub_outline_titles[i]:
                    SubOutline.objects.get_or_create(
                        course_outline=outline,
                        sub_title=sub_outline_title
                    )

            self.stdout.write(self.style.SUCCESS("Successfully populated outlines and sub-outlines for Internet of Things BootCamp."))
