from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users, Trip
from .serializers import DetailSerializer, UserSerializer


class ListUsersView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class ListTripsView(generics.ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = DetailSerializer


'''@api_view(['GET'])
def detail_collection(request):
    if request.method == 'GET':
        data = Detail.objects.all()
        serializer = DetailSerializer(data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def detail_element(request, pk):
    try:
        details = Detail.objects.get(pk=pk)
    except Detail.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DetailSerializer(details)
        return Response(serializer.data)'''