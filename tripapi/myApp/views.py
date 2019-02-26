from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from .models import User_Details, Trip
from .serializers import UserSerializer, TripSerializer


class UsersView(APIView):
    def get(self, request):
        users = User_Details.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})

class PostUsersView(APIView):

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteUsersView(APIView):

    def get_object(self, pk):
        try:
            return User_Details.objects.get(pk=pk)
        except User_Details.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
        
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class TripsView(APIView):

    def get(self, request):
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response({"trips": serializer.data})

class PostTripsView(APIView):

    def post(self, request, format=None):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class EditTripsView(APIView):

    def get_object(self, pk):
        try:
            return Trip.objects.get(pk=pk)
        except Trip.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        trip = self.get_object(pk)
        serializer = TripSerializer(trip)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        trip = self.get_object(pk=pk)
        serializer = TripSerializer(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteTripsView(APIView):

    def get_object(self, pk):
        try:
            return Trip.objects.get(pk=pk)
        except Trip.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        trip = self.get_object(pk)
        serializer = TripSerializer(trip)
        return Response(serializer.data)
        
    def delete(self, request, pk, format=None):
        trip = self.get_object(pk)
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    