from django.db import models

class Collages(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    enrollment_date = models.DateField()
    
    def __str__(self):
        return self.name
