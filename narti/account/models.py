from django.db import models
from django.urls import reverse


class Comics(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    lang = models.CharField(max_length=3)
    is_published = models.BooleanField(default=True)


def __str__(self):
    return self.title


def get_absolute_url(self):
    return reverse('post', kwargs={'coms_id': self.pk})
