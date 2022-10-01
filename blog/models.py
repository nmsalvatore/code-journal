from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db import models
from datetime import timedelta

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    slug = models.SlugField(null=True, unique=True)

    @property
    def is_updated(self):
        publish_window = self.date_created + timedelta(seconds=1)
        return self.date_updated > publish_window

    def __str__(self) -> str:
        return self.body

    def get_absolute_url(self):
        return reverse('view-post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_created']