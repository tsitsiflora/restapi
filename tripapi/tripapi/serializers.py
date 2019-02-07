from rest_framework import serializers
from .models import Details


class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Details
        fields = ('trip_id', 'driver_name', 'reg_number', 'opening_milage', 'closing_milage', 'destination', 'comments', 'date')