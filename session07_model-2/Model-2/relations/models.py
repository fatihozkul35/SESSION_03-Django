from pyexpat import model
from django.db import models



class Creator(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name

class Language(models.Model):    
    name = models.CharField(max_length=50)
    producer = models.OneToOneField(Creator, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name


class Frameworks(models.Model):                
    name= models.CharField(max_length=40)
    dil = models.ForeignKey(Language, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

#* on delete methods
# CASCADE
# PROTECT
# SET_NULL  -null=True
# SET_DEFAULT - default=...
# DO_NOTHİNG

class Developers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    framework = models.ManyToManyField(Frameworks)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"    

