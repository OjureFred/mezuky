from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    path('api/', views.apiOverview, name='api'),
    path('channels-list/', views.channelsList, name='channels-list'),
    path('channel-detail/<str:pk>/', views.channelDetail, name='channel-detail'),
    path('channel-create/', views.channelCreate, name='channel-create'),
    path('channel-update/<str:pk>/', views.channelUpdate, name='channel-update'),
    path('channel-delete/<str:pk>/', views.channelDelete, name='channel-delete'),

    path('songs-list/', views.songsList, name='songs-list'),
    path('song-detail/<str:pk>/', views.songDetail, name='song-detail'),
    path('song-create/', views.songCreate, name='song-create'),
    path('song-update/<str:pk>/', views.songUpdate, name='song-update'),
    path('song-delete/<str:pk>/', views.songDelete, name='song-delete'),

    path('plays-list/', views.playsList, name='plays-list'),

]