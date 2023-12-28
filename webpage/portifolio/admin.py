from django.contrib import admin
from .models import (
    Profile, 
    Project,
    Technology,
    ProfileLink,
    ProjectAsset,
    ProjectDetail,
    ProjectTechnology,
)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(ProfileLink)
admin.site.register(ProjectAsset)
admin.site.register(ProjectDetail)
admin.site.register(ProjectTechnology)
