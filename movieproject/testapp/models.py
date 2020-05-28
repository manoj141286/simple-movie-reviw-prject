from django.db import models

# Create your models here.
class movie(models.Model):
    ReleaseDate=models.DateField()
    MovieName=models.CharField(max_length=30)
    Hero=models.CharField(max_length=30)
    Heroine=models.CharField(max_length=30)
    Rating=models.IntegerField()
    
