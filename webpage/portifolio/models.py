from django.db import models
from articles.models import Model, ARTICLE_TYPE_CHOICES



STUDY_SUBJECT_CHOICES = ARTICLE_TYPE_CHOICES
STUDY_TYPE_CHOICES = (
    ('vid', 'Video'),
    ('ppr', 'Papers'),
    ('art', 'Artigos'),
    ('blg', 'Blog Post'),
    ('col', 'Colaborações'),
    ('tst', 'Testes Pessoais'),
)
class Study(Model):
    url = models.URLField()
    thought = models.TextField()
    description = models.TextField()
    title = models.CharField(max_length=255)
    technologies = models.ManyToManyField('projects.Technology')
    created_at = models.DateTimeField(auto_now_add=True) 
    study_type = models.CharField(choices=STUDY_TYPE_CHOICES)
    study_subject = models.CharField(choices=STUDY_SUBJECT_CHOICES)

    class Meta:
        default_related_name = 'studies'
        ordering = ('created_at',)

    def __str__(self):
        return self.title
