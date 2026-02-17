from django.db import models

class articles(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True)
    # image = models.ImageField(upload_to='articles/', blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100, default='Admin',blank=True, null=True)

    def __str__(self):
        return self.title

