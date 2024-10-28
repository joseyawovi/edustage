from django.core.management.base import BaseCommand
from ...models import Course, Outline, SubOutline  # Update with the correct model path

class Command(BaseCommand):
    help = 'Populate the Generative AI BootCamp course with outlines and sub-outlines'

    def handle(self, *args, **kwargs):
        try:
            generative_ai_bootcamp = Course.objects.get(title='Generative AI BootCamp')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR("The course 'Generative AI BootCamp' does not exist. Please create the course first."))
        else:
            outline_titles = [
                'Introduction to Generative AI', 
                'Generative Models Overview', 
                'Deep Generative Models',
                'Generative Adversarial Networks (GANs)',
                'Variational Autoencoders (VAEs)', 
                'Applications of Generative AI'
            ]

            sub_outline_titles = [
                ['What is Generative AI?', 'History and Evolution', 'Applications in Industry'],
                ['Types of Generative Models', 'Comparison of Approaches', 'Use Cases'],
                ['Understanding Neural Networks', 'Training Deep Models', 'Evaluating Generative Models'],
                ['Architecture of GANs', 'Training GANs', 'Applications of GANs'],
                ['Architecture of VAEs', 'Training VAEs', 'Applications of VAEs'],
                ['Creative AI', 'Generative AI in Media', 'Ethics in Generative AI']
            ]

            for i, outline_title in enumerate(outline_titles):
                outline, created = Outline.objects.get_or_create(
                    course=generative_ai_bootcamp,
                    title=outline_title,
                    description=f"This is the outline for {outline_title} in the Generative AI BootCamp course."
                )

                for sub_outline_title in sub_outline_titles[i]:
                    SubOutline.objects.get_or_create(
                        course_outline=outline,
                        sub_title=sub_outline_title
                    )

            self.stdout.write(self.style.SUCCESS("Successfully populated outlines and sub-outlines for Generative AI BootCamp."))
