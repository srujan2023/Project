from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=100)
    Realse_date = models.DateField(null=True,blank=True)
    language = models.CharField(null=True,blank=True)   
    Hero = models.CharField(null=True,blank=True)
    budget = models.IntegerField(null=True,blank=True)
    Collection = models.IntegerField(null=True,blank=True) 
    def __str__(self):
        return self.name
