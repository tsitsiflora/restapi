from rest_framework import serializers
from .models import Users, Trip


class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ('trip_id', 'driver_name', 'reg_number', 'opening_milage', 'closing_milage',
             'destination', 'comments', 'date')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('user_id', 'name', 'username', 'password')