from django.db import models


class Comics(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    lang = models.CharField(max_length=3)
    is_published = models.BooleanField(default=True)


def __str__(self):
    return self.title
