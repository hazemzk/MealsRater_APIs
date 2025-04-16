from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2, default= 0 )
    description = models.TextField(max_length=360)
    
    def no_of_rating(self):
        ratings = Rating.objects.filter(meal=self)
        return len(ratings)
    
    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(meal=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) == 0:
            return 0
        else:
            return sum / len(ratings)
        
    
    def __str__(self):
        return self.name
    
    
class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    class meta:
        unique_together =(('user' , 'meal'),)
        index_together =(('user' , 'meal'),)