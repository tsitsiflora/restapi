from rest_framework import serializers
from .models import User_Details, Trip


class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ('trip_id', 'driver_name', 'reg_number', 'opening_milage', 'closing_milage',
             'destination', 'comments', 'date')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Details
        fields = ('user_id', 'name', 'username', 'password')