from django.db import models
from projects.models import Model, PROJECT_TYPE_CHOICES

# Create your models here.
ARTICLE_TYPE_CHOICES = PROJECT_TYPE_CHOICES + (
    ('career', 'Carreira'),
    ('community', 'Comunidade'),
    ('sdev', 'Desenvolvimento de Software')
)
class Article(Model):
    url = models.URLField()
    description = models.TextField()
    title = models.CharField(max_length=255)
    technologies = models.ManyToManyField('projects.Technology')
    created_at = models.DateTimeField(auto_now_add=True)
    article_type = models.CharField(
        choices=ARTICLE_TYPE_CHOICES, 
        max_length=32
    )

    class Meta:
        default_related_name = 'articles'
        ordering = ('-created_at',)
        verbose_name = 'artigo'
        verbose_name_plural = 'artigos'

    def __str__(self):
        return self.title
