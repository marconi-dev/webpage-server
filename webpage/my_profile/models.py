from uuid import uuid4
from django.db import models


class Model(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        editable=False,
        default=uuid4
    )
    class Meta:
        abstract = True


class Profile(Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    titles = models.CharField(max_length=255)

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfil" # Must not have plural name

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

    class Meta:
        verbose_name = "link de perfil"
        verbose_name_plural = "links de perfil"

    def __str__(self):
        return f"{self.name} - URL"
