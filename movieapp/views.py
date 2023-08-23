from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MovieForm
from . models import movie
# Create your views here.
def index(request):
    Movies=movie.objects.all()
    context={
        'movie_list':Movies
    }
    return render(request,"index.html",context)
def detail(request,movie_id):
     MOVIE=movie.objects.get(id=movie_id)
     # return HttpResponse("this is the movie No %s"% movie_id)

     return render(request,"detail.html",{"movie":MOVIE})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        disc=request.POST.get('disc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        MOVIE=movie(name=name,disc=disc,year=year,img=img)
        MOVIE.save()
    return render(request,'add.html')
def update_movies(request,id):
    Movies=movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=Movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':Movies})
def delete_func(request,id):
    if request.method=='POST':
        movie_delete=movie.objects.get(id=id)
        movie_delete.delete()
        return redirect('/')
    return render(request,'delete.html')
