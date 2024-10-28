from django.core.management.base import BaseCommand
from ...models import Course, Outline, SubOutline  # Update with the correct model path

class Command(BaseCommand):
    help = 'Populate the AI BootCamp course with outlines and sub-outlines'

    def handle(self, *args, **kwargs):
        try:
            ai_bootcamp = Course.objects.get(title='AI BootCamp')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR("The course 'AI BootCamp' does not exist. Please create the course first."))
        else:
            outline_titles = [
                'Introduction to AI', 
                'Machine Learning Basics', 
                'Deep Learning', 
                'Natural Language Processing', 
                'Computer Vision',
                'AI Ethics and Future Trends'
            ]

            sub_outline_titles = [
                ['What is AI?', 'History of AI', 'Applications of AI'],
                ['Supervised Learning', 'Unsupervised Learning', 'Reinforcement Learning'],
                ['Neural Networks', 'Convolutional Neural Networks', 'Recurrent Neural Networks'],
                ['Text Processing', 'Sentiment Analysis', 'Language Models'],
                ['Image Processing', 'Object Detection', 'Image Classification'],
                ['Ethics in AI', 'Future of AI', 'AI in Society']
            ]

            for i, outline_title in enumerate(outline_titles):
                outline, created = Outline.objects.get_or_create(
                    course=ai_bootcamp,
                    title=outline_title,
                    description=f"This is the outline for {outline_title} in the AI BootCamp course."
                )

                for sub_outline_title in sub_outline_titles[i]:
                    SubOutline.objects.get_or_create(
                        course_outline=outline,
                        sub_title=sub_outline_title
                    )

            self.stdout.write(self.style.SUCCESS("Successfully populated outlines and sub-outlines for AI BootCamp."))
