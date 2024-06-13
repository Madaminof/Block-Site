from django.urls import path
from .views import CategoryView, PostView, LatestNewsView, ProfileView, like_post,TopLikesProducts

app_name = 'posts'

urlpatterns = [
    path('category/', CategoryView.as_view(),name='category'),
    path('post/<int:pk>', PostView.as_view(),name='post'),
    path('songgiyangilik/',LatestNewsView.as_view(),name='songgiyangilik'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('like/<int:pk>', like_post, name='like_post'),
    path('top_like/',TopLikesProducts.as_view(),name='top_like'),
    ]