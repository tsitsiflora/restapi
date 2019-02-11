from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    password = serializers.CharField()

class TripSerializer(serializers.Serializer):
    trip_id = serializers.IntegerField()
    driver_name = serializers.CharField(max_length=255)
    reg_number = serializers.CharField(max_length=255)
    opening_milage = serializers.IntegerField()
    closing_milage = serializers.IntegerField()
    destination = serializers.CharField(max_length=255)
    comments = serializers.CharField(max_length=500)
    date = serializers.DateField()


