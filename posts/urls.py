from django.urls import path
from .views import CategoryView,PostView,LatestNewsView,ProfileView

urlpatterns = [
    path('category/', CategoryView.as_view(),name='category'),
    path('post/<int:pk>', PostView.as_view(),name='post'),
    path('songgiyangilik/',LatestNewsView.as_view(),name='songgiyangilik'),
    path('profile/',ProfileView.as_view(),name='profile'),
    ]