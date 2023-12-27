from django.contrib import admin
from .models import (
    Profile, 
    ProfileLink,
    Project,
    Technology,
    ProjectAsset,
    ProjectDetail,
)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(ProfileLink)
admin.site.register(ProjectAsset)
admin.site.register(ProjectDetail)
