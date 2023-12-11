from django.db import models

# Create your models here.

class Booktable(models.Model):
    table = models.CharField(max_length=100)
    no_of_people = models.IntegerField()
    image = models.ImageField(upload_to='static/images/')
    description= models.CharField(max_length=100)
    # price = models.IntegerField(max_length=100)
    
    def __str__(self):
        return self.table
    