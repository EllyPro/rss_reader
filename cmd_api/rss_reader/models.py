from django.db import models

# Create your models here.


class Feeds(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    link = models.CharField(max_length=200, blank=True, default='')
    updated = models.DateTimeField()
    summary = models.TextField()
    content = models.TextField()

    class Meta:
        ordering = ['updated']

    def __str__(self):
        return self.title