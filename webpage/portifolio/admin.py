from django.contrib import admin
from .models import (
    Study,
    Article,
)

# Register your models here.
admin.site.register(Study)
admin.site.register(Article)
