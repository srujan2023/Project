from django.conf import settings
from django.db import models

class articles(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100, default='Admin',blank=True, null=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_articles',
        blank=True
    )
    dislikes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='disliked_articles',
        blank=True
    )

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

