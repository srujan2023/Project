from django.db import models

class Teachers(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    enrollment_date = models.DateField()
    Address = models.CharField(max_length=100)
    
    DOB = models.DateField()
    Teacher_id = models.IntegerField()
    
    Collage_Name = models.CharField()
    
    Gender = models.CharField()
    
    def __str__(self):
        return self.name
