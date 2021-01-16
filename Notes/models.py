from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField(blank = True, null = True)
    slug = models.SlugField(max_length = 100, unique = True)

    class Meta:
        ordering = ('title',)