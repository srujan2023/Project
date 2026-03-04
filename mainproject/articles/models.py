from django.conf import settings
from django.db import models

class articles(models.Model):
    VISIBILITY_PUBLIC = 'public'
    VISIBILITY_PRIVATE = 'private'
    VISIBILITY_CHOICES = (
        (VISIBILITY_PUBLIC, 'Public'),
        (VISIBILITY_PRIVATE, 'Private'),
    )

    title = models.CharField(max_length=200,blank=True, null=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100, default='Admin',blank=True, null=True)
    visibility = models.CharField(
        max_length=10,
        choices=VISIBILITY_CHOICES,
        default=VISIBILITY_PUBLIC,
    )
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

