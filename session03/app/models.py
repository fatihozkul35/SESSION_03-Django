from django.db import models

# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30,null=True)
    age = models.IntegerField(primary_key=True)
    date_time = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True, null=False)
    about_me = models.TextField(max_length=50,null=True)
    avatar = models.ImageField(null=True, upload_to='media/')


    def __str__(self):
        return f"{self.age} - {self.first_name} - {self.last_name} - {self.date_time} - {self.last_update} - {self.about_me} - {self.avatar}"
