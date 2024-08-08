from django.db import models
# this imports use to generate token auto with new user
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token
# //
from django.contrib.auth.models import User

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


# this function create token with every new user   
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def tokenCreate(sender,instance,created, **Kwargs):
    if created:
        Token.objects.create(user=instance)



# this class used our permissions 
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    