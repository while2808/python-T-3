from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    # return HttpResponse('<h1>This is my home page </h1>')
    # return render(request,'home.html')
    searchTerm=request.GET.get('searchMovie')
    if searchTerm:
        movies=Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies=Movie.objects.all()
    return render(request,'home.html',{'searchTerm':searchTerm,'name':'Harnish','movies':movies})

def about(request):
    return HttpResponse('<h1>This is about page</h1>')


def signup(request):
    email=request.GET.get('email')
    return render(request,'signup.html',{'email':email})


def detail(request,id):
    movie=get_object_or_404(Movie,pk=id)
    return render(request,'details.html',{'movie':movie})
