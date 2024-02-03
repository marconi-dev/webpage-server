from django.db import models
from articles.models import Model, ARTICLE_TYPE_CHOICES

# Create your models here.
STUDY_SUBJECT_CHOICES = ARTICLE_TYPE_CHOICES
STUDY_TYPE_CHOICES = (
    ("vid", "Video"),
    ("ppr", "Papers"),
    ("art", "Artigos"),
    ("blg", "Blog Post"),
    ("col", "Colaborações"),
    ("tst", "Testes Pessoais"),
)


class Study(Model):
    url = models.URLField()
    thought = models.TextField(blank=True, null=True)
    description = models.TextField()
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    technologies = models.ManyToManyField("projects.Technology")
    study_type = models.CharField(choices=STUDY_TYPE_CHOICES, max_length=32)
    study_subject = models.CharField(choices=STUDY_SUBJECT_CHOICES, max_length=32)

    class Meta:
        default_related_name = "studies"
        ordering = ("-created_at",)
        verbose_name = "estudo"
        verbose_name_plural = "estudos"

    def __str__(self):
        return self.title
