from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User_Details, Trip
from .serializers import UserSerializer, TripSerializer


class ListUsersView(APIView):
    def get(self, request):
        users = User_Details.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})
    

class ListTripsView(APIView):
    def get(self, request):
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response({"trips": serializer.data})
    