from django.db import models
from django.urls import reverse


class Comics(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    is_published = models.BooleanField(default=True)
    language = models.ForeignKey('Language', on_delete=models.PROTECT, null=True)
    gender = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('comics_id', kwargs={'coms_id': self.pk})


class Language(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    abbr = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('language', kwargs={'lang_id': self.pk})
