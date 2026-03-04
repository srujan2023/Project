from django.db import models

class Shopping(models.Model):
    VISIBILITY_PUBLIC = 'public'
    VISIBILITY_PRIVATE = 'private'
    VISIBILITY_CHOICES = (
        (VISIBILITY_PUBLIC, 'Public'),
        (VISIBILITY_PRIVATE, 'Private'),
    )

    Productname = models.CharField(max_length=100)
    Price = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    visibility = models.CharField(
        max_length=10,
        choices=VISIBILITY_CHOICES,
        default=VISIBILITY_PUBLIC,
    )

    def __str__(self):
        return self.Productname

