from distutils.command.upload import upload
from django.db import models


class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
    ]
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    number = models.IntegerField()
    about = models.TextField(null=True, blank=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='media/')
    register_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
    year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, default="FR")

    
    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Öğrenciler"
        db_table = "Student_Table"
        
    
    
    