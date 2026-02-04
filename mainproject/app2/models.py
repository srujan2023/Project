from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True,blank=True)
    enrollment_date = models.DateField(null=True,blank=True)
    Address = models.CharField(null=True,blank=True)
    DOB = models.DateField(null=True,blank=True)
    Students_id = models.IntegerField(null=True,blank=True)
    Collage_Name = models.CharField(null=True,blank=True)
    Gender = models.CharField(null=True,blank=True)
    def  __str__(self):
      return self.name
