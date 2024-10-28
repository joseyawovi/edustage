from django.core.management.base import BaseCommand
from ...models import Course, Outline, SubOutline  # Update with the correct model path

class Command(BaseCommand):
    help = 'Populate the System Administration BootCamp course with outlines and sub-outlines'

    def handle(self, *args, **kwargs):
        try:
            system_admin_bootcamp = Course.objects.get(title='System Administration')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR("The course 'System Administration' does not exist. Please create the course first."))
        else:
            outline_titles = [
                'Introduction to System Administration', 
                'Operating System Management', 
                'User and Group Management',
                'Network Configuration', 
                'Security and Compliance', 
                'Backup and Recovery Strategies'
            ]

            sub_outline_titles = [
                ['Role of a System Administrator', 'Key Responsibilities', 'Importance of System Administration'],
                ['Installing Operating Systems', 'System Updates and Patches', 'Monitoring System Performance'],
                ['Creating Users and Groups', 'Managing Permissions', 'User Account Policies'],
                ['Configuring Network Settings', 'Understanding TCP/IP', 'Network Troubleshooting'],
                ['Implementing Security Measures', 'Compliance Standards', 'Auditing and Monitoring'],
                ['Backup Solutions', 'Disaster Recovery Planning', 'Testing Backup Procedures']
            ]

            for i, outline_title in enumerate(outline_titles):
                outline, created = Outline.objects.get_or_create(
                    course=system_admin_bootcamp,
                    title=outline_title,
                    description=f"This is the outline for {outline_title} in the System Administration BootCamp course."
                )

                for sub_outline_title in sub_outline_titles[i]:
                    SubOutline.objects.get_or_create(
                        course_outline=outline,
                        sub_title=sub_outline_title
                    )

            self.stdout.write(self.style.SUCCESS("Successfully populated outlines and sub-outlines for System Administration BootCamp."))
