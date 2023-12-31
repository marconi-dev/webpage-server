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


class Profile(Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    titles = models.CharField(max_length=255)

    def __str__(self):
        return f"Profile - {self.name}"


class ProfileLink(Model): 
    url = models.URLField()
    name = models.CharField(max_length=32)
    profile = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE,
        related_name='links'
    )

    def __str__(self):
        return f"{self.name} - URL"


class Technology(Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


PROJECT_TYPE_CHOICES = (
    ('fun', 'For Fun'),
    ('backend', 'Back-End'),
    ('cs', 'Computer Science'),
)
class Project(Model):
    first_commit = models.DateField()
    last_commit = models.DateField()
    name = models.CharField(max_length=32)
    short_description = models.TextField()
    is_active = models.BooleanField(default=True)
    deploy = models.URLField(blank=True, null=True)
    source_code = models.URLField(blank=True, null=True)
    project_type = models.CharField(choices=PROJECT_TYPE_CHOICES)
    tecnologies = models.ManyToManyField(
        Technology, 
        through='portifolio.ProjectTechnology',
    )

    def __str__(self):
        return self.name


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

    def __str__(self):
        return f"{self.project.name} - {self.technology.name}"


class ProjectAsset(ProjectDetailMixin):
    image = models.ImageField(blank=True, null=True)
    alter_text = models.TextField(blank=True, null=True)
    mobile_image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        default_related_name = "assets"

    def __str__(self):
        return f"{self.project.name} - {self.title}: {self.image.name}"


class ProjectDetail(ProjectDetailMixin):
    title = models.CharField(max_length=255)

    class Meta:
        default_related_name = "details"

    def __str__(self):
        return f"{self.project.name} - {self.title}"
