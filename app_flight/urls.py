
from django.contrib import admin
from django.urls import path

from app_flight.views import (
   AirportListCreateView,
   AirportUpdateDeteletGetView,
   AircraftListCreateView,
   AircraftUpdateDeteletGetView,
   FlightListCreateView,
   FlightUpdateDeteletGetView,
   Flight_Report_View)

urlpatterns = [

    # Airport URL
    path("Airport_create_list/", AirportListCreateView.as_view()),
    path("Airport/<int:pk>/",
         AirportUpdateDeteletGetView.as_view()),

     

    # Aircraft URL
    path("Aircraft_create_list/", AircraftListCreateView.as_view()),
    path("Aircraft/<int:pk>/",
         AircraftUpdateDeteletGetView.as_view()),

    # Flight URL
    path("Flight_create_list/", FlightListCreateView.as_view()),
    path("Flight-Update-get-delete/<int:pk>/",
         FlightUpdateDeteletGetView.as_view()),
    path("Flight-Report/",
         Flight_Report_View.as_view()),
     
]
