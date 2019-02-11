from rest_framework import serializers
from .models import Trip, User_Details


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

    def create(self, validated_data):
        return Trip.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.trip_id = validated_data.get('trip_id', instance.trip_id)
        instance.driver_name = validated_data.get('driver_name', instance.driver_name)
        instance.reg_number = validated_data.get('reg_number', instance.reg_number)
        instance.opening_milage = validated_data.get('opening_milage', instance.opening_milage)
        instance.closing_milage = validated_data.get('closing_milage', instance.closing_milage)
        instance.destination = validated_data.get('destination', instance.destination)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.date = validated_data.get('date', instance.date)

        instance.save()
        return instance


