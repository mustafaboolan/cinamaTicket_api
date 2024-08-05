from rest_framework import serializers
from . import models

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'



class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = '__all__'    
        


class QuestSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Quest
        fields = ['pk','name','mobile']          