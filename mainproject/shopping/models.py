from django.db import models

class Shopping(models.Model):
    Productname = models.CharField(max_length=100)
    Price = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.Productname

