from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    class Meta:
        ordering = ['-datetime_created']