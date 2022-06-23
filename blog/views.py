from django.shortcuts import render
from . models import Post


def post (request):
    data=Post.objects.all()
    return render (request, 'blog/home.html',{'posts':data})


def about (request):
    return render (request,'blog/about.html',{'title':'about'})

