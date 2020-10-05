from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    path('api/', views.apiOverview, name='api'),
    path('channels-list/', views.channelsList, name='channels-list'),
    path('channel-detail/<str:pk>/', views.channelDetail, name='channel-detail'),
    path('channel-create/', views.channelCreate, name='channel-create'),
    path('channel-update/<str:pk>/', views.channelUpdate, name='channel-update'),

]