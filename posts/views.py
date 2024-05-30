from django.shortcuts import render
from django.views import View

from .models import Category, Post,LatestNews,Profile


# Create your views here.


class CategoryView(View):
    def get(self,request):
        categories = Category.objects.all()
        return render(request,'category.html',{'categories': categories})


class PostView(View):
    def get(self,request, pk):
        posts = Post.objects.filter(category=pk)
        return render(request,'post.html',{'posts': posts})


class LatestNewsView(View):
    def get(self,request):
        post = LatestNews.objects.all()
        return render(request,'songgi_yangilik.html',{'post': post})




class ProfileView(View):
    def get(self,request):
        profile = Profile.objects.all()
        return render(request,'profile.html',{'profile': profile})
