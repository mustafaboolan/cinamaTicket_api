from django.db import models

# Create your models here.
class Movie(models.Model):
    hall = models.CharField(max_length=30)
    movie_name = models.CharField(max_length=30)
    # date = models.DateField()
    def __str__(self):
        return self.movie_name

class Quest(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Reservation (models.Model):
    quest =models.ForeignKey(Quest,related_name='reservation',on_delete=models.CASCADE)
    movie =models.ForeignKey(Movie,related_name='reservation',on_delete=models.CASCADE)
    # def __str__ (self):
    #     return self.movie

   