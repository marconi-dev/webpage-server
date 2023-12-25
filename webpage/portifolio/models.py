from django.db import models

# Create your models here.
class Profile(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    titles = models.CharField(max_length=255)

    def __str__(self):
        return f"Profile - {self.name}"


class ProfileLink(models.Model): 
    url = models.URLField()
    name = models.CharField(max_length=32)
    profile = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE,
        related_name='links'
    )

    def __str__(self):
        return f"{self.name} - URL"
