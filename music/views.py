from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse('<h1>hello world</h1>')


def detail(request, album_id):
	return HttpResponse('<h2>This is album_id:' + str(album_id) + '</h2>')