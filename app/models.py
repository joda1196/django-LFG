from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    header = models.TextField(max_length=100)
    PLATFORMS = (
        ("XBOX", "XBOX"),
        ("PLAYSTATION", "PLAYSTATION"),
        ("STEAM", "STEAM"),
    )
    platform = models.CharField(max_length=50, choices=PLATFORMS)
    # Fields Below need to hidden and autofilled
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    time_posted = models.DateTimeField(blank=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return f"{self.platform}|{self.author.username}"

    class Meta:
        ordering = ["-time_posted"]
