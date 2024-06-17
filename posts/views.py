from django.shortcuts import render
from django.views import View

from .models import Category, Post,LatestNews

class CategoryView(View):
    def get(self,request):
        categories = Category.objects.all()
        product = Post.objects.all().order_by('-data')
        yangilik = LatestNews.objects.all()
        return render(request,'base.html', {'categories': categories,'product': product, 'yangilik':yangilik})


class PostView(View):
    def get(self,request, pk):
        posts = Post.objects.filter(category=pk)
        return render(request,'post.html',{'posts': posts})


class LatestNewsView(View):
    def get(self,request):
        post = LatestNews.objects.all()
        return render(request,'base.html',{'post': post})


class SaytHaqida(View):
    def get(self,request):
        return render(request,'sayt_haqida.html')

