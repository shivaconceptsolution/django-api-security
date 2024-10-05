from django.db import models

class MyData(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    
    def __str__(self):
        return self.name
