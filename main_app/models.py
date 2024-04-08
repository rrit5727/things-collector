from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=20)
    breed = models.CharField(max_length=20)
    description = models.TextField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    