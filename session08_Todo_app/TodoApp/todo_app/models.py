from django.db import models


class Todo(models.Model):  # appname_modelname
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_date',)
        # db_table = "Yapılacaklar"
