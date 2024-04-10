from django.db import models
from django.urls import reverse

MEALS = (
    ( 'B ', 'Breakfast'),
    ( 'L', 'Lunch'),
    ( 'D', 'Dinner')
)

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=20)
    breed = models.CharField(max_length=20)
    description = models.TextField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})
    

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=20,
        choices=MEALS,
        default=MEALS[0][0]
    )

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Park(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    offleash = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('parks_detail', kwargs={'pk': self.id}
        )
    
