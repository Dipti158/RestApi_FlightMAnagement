from django.shortcuts import render


# Permission Class
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

# OS
import os


# Swaggers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Simple Json Web Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics
# Serializers
from app_flight.serializers import (
    AirportSerializers,
    AircraftSerializers,
    FlightSerializers
)

from app_flight.models import Airport,Aircraft,Flight

from rest_framework.filters import SearchFilter

from rest_framework import status 
from rest_framework import response
from rest_framework.response import Response

from django.db.models import Q 

from rest_framework.views import APIView

from datetime import datetime, timedelta
import urllib.parse
from django.utils import timezone

from django.db import connection

"""
******************************************************************************************************************
                                        Airport
******************************************************************************************************************
"""

# Airport View For Create And List
class AirportListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]
    queryset = Airport.objects.all()
    serializer_class = AirportSerializers
      
    
# # Airport View For Update,Delete and Get
class AirportUpdateDeteletGetView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]
    queryset = Airport.objects.all()
    serializer_class = AirportSerializers


"""
******************************************************************************************************************
                                       Aircraft
******************************************************************************************************************
"""

# Airport View For Create And List
class AircraftListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializers
      
    
# # Airport View For Update,Delete and Get
class AircraftUpdateDeteletGetView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializers



"""
******************************************************************************************************************
                                       Flight
******************************************************************************************************************
"""

# Airport View For Create And List
class FlightListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers

    filter_backends = [SearchFilter]
    search_fields = ['Departure_airport__ICAO_Code',
                     'Arrival_airport__ICAO_Code']
      
    
# # Airport View For Update,Delete and Get
class FlightUpdateDeteletGetView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers

    filter_backends = [SearchFilter]
    search_fields = ['Departure_airport__ICAO_Code',
                     'Arrival_airport__ICAO_code']


#
class Flight_Report_View(APIView):
    serializer_class = FlightSerializers
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        response = {
            'status': 1,
            'message': 'successfully retrived flights',
            'data': {},
        }
        Departure_Datetime = request.query_params.get('Departure_Datetime')
        Arrival_Datetime = request.query_params.get('Arrival_Datetime')
        print(Departure_Datetime)
        print(Arrival_Datetime)

        try:
            print(">>>>>>>>>>>> To Check ?>>>>>>>>>>>>>>>>>")
            queryset = (
                Flight.objects.select_related('Flight', 'Departure_airport').filter(Q(Departure_Datetime__gte=Departure_Datetime) & Q(
                    Arrival_Datetime__lte=Arrival_Datetime)).order_by('Departure_airport')
            )
        except ValueError:
            return Response(
                'invalid parameters', status=status.HTTP_400_BAD_REQUEST
            )
        data = {}
        for flight in queryset:
            if not data.__contains__(flight.Departure_airport.ICAO_Code):
                flight_time_for_each_aircraft = []
                data[flight.Departure_airport.ICAO_Code] = {
                    'airport_name': flight.Departure_airport.Airport_Name,
                    'flights_count': 0,
                    'flight_time_for_each_aircraft': flight_time_for_each_aircraft,
                }
            data[flight.Departure_airport.ICAO_Code]['flights_count'] += 1
            flight_time_for_each_aircraft.append(
                {
                    'aircraft': AircraftSerializers(flight.Flight).data,
                    'flight_time': '{} minutes'.format((flight.Arrival_Datetime -flight.Departure_Datetime).total_seconds()/60
                    ),
                }
            )

        response['data'] = data
        return Response(response)

























# class Flight_Report_View(APIView):
#     serializer_class = FlightSerializers
#     permission_classes = [AllowAny]

#     def get(self, request, format=None, *args, **kwargs):
#         response = {
#             'status': 1,
#             'message': 'successfully retrived flights',
#             'data': {},
#         }

#         # print(request.query_params)
        

#         Departure_Datetime = self.request.query_params.get(
#             'Departure_Datetime')
#         Arrival_Datetime = self.request.query_params.get(
#             'Arrival_Datetime')
        
#         # print(connection.queries)
#         print(Departure_Datetime)
#         print(Arrival_Datetime)

#         try:
#             print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#             queryset = (
#                 Flight.objects.select_related('Flight', 'Departure_airport').filter(Q(Departure_Datetime=Departure_Datetime) & Q(
#                     Arrival_Datetime=Arrival_Datetime)).order_by('Departure_airport')
#             )
#         except ValueError:
#             return Response(
#                 'invalid parameters', status=status.HTTP_400_BAD_REQUEST
#             )
#         data = {}
#         for flight in queryset:
#             if not data._contains_(flight.Departure_airport.ICAO_Code):
#                 flight_time_for_each_aircraft = []
#                 data[flight.Departure_airport.ICAO_Code] = {
#                     'airport_name': flight.Departure_airport.Airport_Name,
#                     'flights_count': 0,
#                     'flight_time_for_each_aircraft': flight_time_for_each_aircraft,
#                 }
#             data[flight.Departure_airport.ICAO_Code]['flights_count'] += 1
#             flight_time_for_each_aircraft.append(
#                 {
#                     'aircraft': AircraftSerializers(flight.Flight).data,
#                     'flight_time': '{} minutes'.format(
#                         (flight.Aparture_Flight_Time -
#                          flight.Departure_Flight_Time).total_seconds()/60
#                     ),
#                 }
#             )

#         response['data'] = data
#         return Response(response)
    


    
    ####################3333333





# 

    

# Given URL with parameters
        # url = "http://127.0.0.1:8000/swagger/?Departure_Datetime=2023-12-12%2008:21:00&Arrival_Datetime=2023-12-16%2008:12:00"

        # # Parsing URL parameters
        # parsed = urllib.parse.urlparse(url)
        # query_params = urllib.parse.parse_qs(parsed.query)

        # # Get the Departure and Arrival Datetime values
        # departure_datetime = query_params.get('Departure_Datetime', [''])[0]
        # arrival_datetime = query_params.get('Arrival_Datetime', [''])[0]

        # # Convert string to datetime object
        # departure_dt = datetime.strptime(departure_datetime, "%Y-%m-%d %H:%M:%S")
        # arrival_dt = datetime.strptime(arrival_datetime, "%Y-%m-%d %H:%M:%S")

        # # Format datetime objects as required
        # formatted_departure = departure_dt.strftime("%b. %d, %Y, %I:%M %p")
        # formatted_arrival = arrival_dt.strftime("%b. %d, %Y, %I:%M %p")

        # print(departure_datetime + "\t" + arrival_datetime)
        # return Response(response)
