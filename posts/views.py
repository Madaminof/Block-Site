from django.shortcuts import render, redirect
from django.views import View

from .models import Category, Post,LatestNews,Profile


# Create your views here.


class CategoryView(View):
    def get(self,request):
        categories = Category.objects.all()
        product = Post.objects.all()
        return render(request,'base.html', {'categories': categories,'product': product})


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

from django.urls import reverse

from django.shortcuts import get_object_or_404, redirect
from .models import Post


def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    return redirect('posts:post', pk=pk)


class TopLikesProducts(View):
    def get(self,request):
        top_likes_products =Post.objects.all()
        top = top_likes_products.order_by('-likes')[:2]
        return render(request,'top_likes.html',{'top': top})
