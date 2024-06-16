from django.urls import path
from .views import CategoryView, PostView, LatestNewsView, SaytHaqida

app_name = 'posts'

urlpatterns = [
    path('', CategoryView.as_view(),name='category'),
    path('post/<int:pk>', PostView.as_view(),name='post'),
    path('songgiyangilik',LatestNewsView.as_view(),name='songgiyangilik'),

    path('sayt', SaytHaqida.as_view(),name='sayt')

    ]