from django.db import models

class articles(models.Model):
    title = models.CharField(null=True,blank=True)
    body = models.CharField(null=True,blank=True)
    image = models.ImageField()
    author = models.CharField(null=True,blank=True)
    
    
    def __str__(self):
        return self.title
