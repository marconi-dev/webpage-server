from django.contrib import admin
from .models import (
    Study,
    Article,
    Project,
    Technology,
    ProjectAsset,
    ProjectDetail,
    ProjectTechnology,
)

# Register your models here.
admin.site.register(Study)
admin.site.register(Project)
admin.site.register(Article)
admin.site.register(Technology)
admin.site.register(ProjectAsset)
admin.site.register(ProjectDetail)
admin.site.register(ProjectTechnology)
