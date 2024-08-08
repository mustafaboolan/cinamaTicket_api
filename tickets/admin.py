from django.contrib import admin

# Register your models here.
from .models import Movie, Post,Quest,Reservation

admin.site.register(Movie)
admin.site.register(Quest)
admin.site.register(Reservation)
admin.site.register(Post)
