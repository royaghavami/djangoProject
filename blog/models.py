from django.db import models
from django.utils import timezone


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published')

    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
# Create your models here.
