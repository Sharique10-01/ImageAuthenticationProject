from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render
from .models import Movie

def home(request):
  return render(request,'authenticationproj/index.html')

def signin(request):
  return render(request,'authenticationproj/signin.html')

def signup(request):
  return render(request,'authenticationproj/signup.html')

def search(request):
  return render(request,'authenticationproj/search.html')

def authenticationproj(request):
  data=Movie.objects.all() #  will generate a query to get all the data from the detabase 
  return render(request,'authenticationproj/home.html',{'movies':data})

def details(request,id):
  data=Movie.objects.get(pk=id) #  will generate a query to get all the data from the detabase 
  return render(request,'authenticationproj/details.html',{'movies':data})

def delete(request,id):
    try:
      movie = Movie.objects.get(pk=id) #if unknown id id provided through the url if its not in the database prompt not found
    except:
      raise Http404('Movie Does not Exist In our Server')
    movie.delete() # else delete the requested movie from the server
    return HttpResponseRedirect('/authenticationproj')

def add(request):
  #getting data from the browser ussing http post method
  title = request.POST.get('title')
  year = request.POST.get('year')
  #if the user had entered any data it shoud be added in the db and then rendered
  if title and year :
    #create an obj of class Movie and then send it to be rendered
    movie=Movie(title=title,year=year)
    movie.save()
    return HttpResponseRedirect('/authenticationproj') #this page appears after data is added
  return render(request,'authenticationproj/add.html')
