from django.urls import path
from .views import *
urlpatterns=[
    path('BikeList/',BikeList.as_view(),name='BikeList'), 
    path('BikeDetail/<int:pk>', BikeDetail.as_view(),name='BikeDetail'),
    path('register/',register,name='register')
]