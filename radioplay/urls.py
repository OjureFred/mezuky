from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    path('api/', views.apiOverview, name='api'),

]