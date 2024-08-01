from django.contrib import admin
from .models import Profile

# admin.site.register(Profile)

@admin.register(Profile)
class ProfleModelManager(admin.ModelAdmin):
  list_display = ['id', 'name', 'email', 'dob', 'state', 'gender', 'location', 'profile_image', 'resume_file']