from django.urls import path
from .views import *
urlpatterns=[
    path('BikeList/',BikeList.as_view(),name='Bike_List'), 
    path('BikeDetail/<int:pk>', BikeDetail.as_view(),name='Bike_Detail')

]