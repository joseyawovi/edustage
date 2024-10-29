from django.core.management.base import BaseCommand
from classes.models import Category

class Command(BaseCommand):
    help = 'Populate the Category model with predefined computer science categories'

    def handle(self, *args, **options):
        categories = [
            {"name": "Software Development", "description": "Focuses on designing, building, and testing software applications."},
            {"name": "Artificial Intelligence & Machine Learning", "description": "Study and creation of algorithms that allow machines to learn from data."},
            {"name": "Cybersecurity", "description": "Protects computer systems, networks, and data from cyber threats."},
            {"name": "Data Science & Analytics", "description": "Involves extracting insights from large datasets using statistical methods."},
            {"name": "Human-Computer Interaction (HCI)", "description": "Designs and improves user interfaces to ensure user-friendliness."},
            {"name": "Theoretical Computer Science", "description": "Studies foundational principles, algorithms, and computational theory."},
            {"name": "Computer Networks", "description": "Covers design, implementation, and maintenance of networking systems."},
            {"name": "Database Systems", "description": "Involves organization, storage, and retrieval of data through database design."},
            {"name": "Cloud Computing & Distributed Systems", "description": "Focuses on scalable resources and distributed architectures."},
            {"name": "Computer Vision & Image Processing", "description": "Enables computers to interpret and make decisions based on visual data."},
            {"name": "Robotics", "description": "Combines hardware and software to create autonomous machines."},
            {"name": "Quantum Computing", "description": "Uses quantum mechanics to process data in new ways."},
            {"name": "Natural Language Processing (NLP)", "description": "Enables computers to understand and respond to human language."},
        ]

        for category in categories:
            cat, created = Category.objects.get_or_create(
                name=category["name"],
                defaults={"description": category["description"]}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Category "{cat.name}" added successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'Category "{cat.name}" already exists.'))

        self.stdout.write(self.style.SUCCESS('Categories populated successfully.'))
