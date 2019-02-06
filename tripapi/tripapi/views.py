from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tripapi.models import Post
from tripapi.serializers import PostSerializer
from tripapi.forms import PostForm


def home(request):
    tmpl_vars = {'form': PostForm()}
    return render(request, 'tripapi/index.html', tmpl_vars)


@api_view(['GET'])
def detail_collection(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def detail_elemennt(request, pk):
    try:
        details = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(details)
        return Response(serializer.data)