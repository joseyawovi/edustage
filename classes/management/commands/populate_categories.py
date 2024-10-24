from django.core.management.base import BaseCommand
from ...models import Category  # Update with the correct model path

class Command(BaseCommand):
    help = 'Populate categories for various BootCamps'

    def handle(self, *args, **kwargs):
        categories = [
            'Web Development',
            'Artificial Intelligence',
            'Digital Forensics',
            'System Administration',
            'Internet of Things',
            'Soft Skills',
            'Information Technology'
        ]

        for category_name in categories:
            category, created = Category.objects.get_or_create(
                name=category_name,
                description=f"This category includes courses related to {category_name}."
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully created category: {category_name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Category already exists: {category_name}"))

        self.stdout.write(self.style.SUCCESS("All categories have been processed."))
