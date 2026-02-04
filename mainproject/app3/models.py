from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    Founder =  models.CharField(null=True,blank=True)
    Co_Founder = models.CharField(null=True,blank=True)
    Esthablished = models.IntegerField()
    GST = models.CharField(null=True,blank=True)
    Total_employees = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.name
