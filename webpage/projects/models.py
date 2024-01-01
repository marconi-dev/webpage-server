from uuid import uuid4
from django.db import models


class Model(models.Model):
    id = models.UUIDField(
        default=uuid4, 
        primary_key=True, 
        editable=False
    )

    class Meta:
        abstract = True


class Technology(Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "tecnologia"
        verbose_name_plural = "tecnologias"


PROJECT_TYPE_CHOICES = (
    ('fun', 'For Fun'),
    ('backend', 'Back-End'),
    ('cs', 'Computer Science'),
    ('frontend', 'Front-End'),
    ('midend', 'Mid-End')
)
class Project(Model):
    first_commit = models.DateField()
    last_commit = models.DateField()
    description = models.TextField()
    short_description = models.TextField()
    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    deploy = models.URLField(blank=True, null=True)
    source_code = models.URLField(blank=True, null=True)
    project_type = models.CharField(choices=PROJECT_TYPE_CHOICES)
    technologies = models.ManyToManyField(
        Technology, 
        through='projects.ProjectTechnology',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "projeto"
        verbose_name_plural = "projetos"


class ProjectDetailMixin(Model):
    description = models.TextField(blank=True, null=True)
    position = models.SmallIntegerField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        ordering = ('position',)


USED_BY_CHOICES = (
    ('front', 'FrontEnd'),
    ('mobile', 'Mobile'),
    ('qa', 'QA'),
)
class ProjectTechnology(ProjectDetailMixin):
    """
    is_equipe_tech: technology was used by me or another team member
    """
    is_equipe_tech = models.BooleanField(default=False)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    used_by = models.CharField(
        choices=USED_BY_CHOICES, 
        blank=True, 
        null=True
    )

    class Meta:
        default_related_name = "techs"
        verbose_name = "tecnologia do projeto"
        verbose_name_plural = "tecnologias dos projetos"

    def __str__(self):
        return f"{self.project.name} - {self.technology.name}"


class ProjectAsset(ProjectDetailMixin):
    image = models.ImageField(blank=True, null=True)
    alter_text = models.TextField(blank=True, null=True)
    mobile_image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        default_related_name = "assets"
        verbose_name = "asset do projeto"
        verbose_name_plural = "assets dos projetos"


    def __str__(self):
        return f"{self.project.name} - {self.title}: {self.image.name}"


class ProjectDetail(ProjectDetailMixin):
    title = models.CharField(max_length=255)

    class Meta:
        default_related_name = "details"
        verbose_name = "detalhe do projeto"
        verbose_name_plural = "detalhes dos projetos"


    def __str__(self):
        return f"{self.project.name} - {self.title}"
