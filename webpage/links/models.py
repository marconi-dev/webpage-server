from django.db import models
from articles.models import Model


# Create your models here.
class Link(Model):
    url = models.URLField()
    description = models.TextField()
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        default_related_name = "links"
        ordering = ("created_at",)
        verbose_name = "link"
        verbose_name_plural = "links"

    def __str__(self):
        return self.title
