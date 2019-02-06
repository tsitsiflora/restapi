from rest_framework import serializers
from tripapi.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('trip_id', 'driver_name', 'reg_number', 'opening_milage', 'closing_milage', 'destination', 'comments', 'date')