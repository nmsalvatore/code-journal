from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self) -> str:
        return self.body

    def get_absolute_url(self):
        return reverse('view-post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-datetime_created']