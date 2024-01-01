from django.contrib import admin
from projects.models import (
    Project,
    Technology,
    ProjectAsset,
    ProjectDetail,
    ProjectTechnology,
)


admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(ProjectAsset)
admin.site.register(ProjectDetail)
admin.site.register(ProjectTechnology)
