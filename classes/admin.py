from django.contrib import admin
from .models import Course, Outline, SubOutline,Registration, Category
from account.models import CustomUser

# main_app/admin.py
from django.contrib import admin

admin.site.site_header = "MySite Administration"
admin.site.site_title = "MySite Admin Portal"
admin.site.index_title = "Welcome to MySite Admin"

class SubOutlineInline(admin.TabularInline):
    model = SubOutline
    extra = 1  # Number of empty forms shown initially

class OutlineAdmin(admin.ModelAdmin):
    inlines = [SubOutlineInline]  # Adds sub-outline inline within course outline
    
admin.site.register(Course)
admin.site.register(Outline, OutlineAdmin)
admin.site.register(Registration)
admin.site.register(Category)
admin.site.register(CustomUser)
