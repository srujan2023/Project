from django.db import models

class Collages(models.Model):
    name = models.CharField(null=True,blank=True)
    collage_id = models.IntegerField(null=True,blank=True)
    Address = models.CharField(null=True,blank=True)
    Fee = models.IntegerField(null=True,blank=True)
    Total_Students = models.IntegerField(null=True,blank=True)
    Total_Teachers = models.IntegerField(null=True,blank=True)
    
    
    def __str__(self):
        return self.name
