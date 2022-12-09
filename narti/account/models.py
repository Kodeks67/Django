from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Comics(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.TextField(blank=True, verbose_name='Description')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    is_published = models.BooleanField(default=True)
    language = models.ForeignKey('Language', on_delete=models.PROTECT, null=True, verbose_name='Language')
    gender = models.CharField(max_length=4, null=True)

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


def validate_even(value):
    if '@' not in value:
        raise ValidationError(
            _('%(value)s does not contains @'),
            params={'value': value},
        )


class FeedBack(models.Model):
    email = models.EmailField(max_length=254, validators=[validate_even])
    message = models.TextField(blank=False)

    def __str__(self):
        return self.email
