from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .models import Post
from .serializers import DetailSerializer
#from .forms import PostForm


def home(request):
    tmpl_vars = {'form': PostForm()}
    return render(request, 'tripapi/index.html', tmpl_vars)


@api_view(['GET'])
def detail_collection(request):
    if request.method == 'GET':
        data = Detail.objects.all()
        serializer = DetailSerializer(data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def detail_elemennt(request, pk):
    try:
        details = Detail.objects.get(pk=pk)
    except Detail.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DetailSerializer(details)
        return Response(serializer.data)