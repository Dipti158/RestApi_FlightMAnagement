
from rest_framework import serializers
from .models import Aircraft,Airport,Flight
from django.utils import timezone
from datetime import timedelta

from django.db.models import Q
from django.db.models import  Max


# Airport Serializer
class AirportSerializers(serializers.ModelSerializer):

    class Meta:
        model = Airport
        fields = ["id", "Airport_Name","Country","City","ICAO_Code"]
        read_only_fields = ["id", ]

    def validate(self, attrs):
        icao_code = attrs.get('ICAO_Code')

        city = attrs.get('City')
        if city and not city.isalpha():
            raise serializers.ValidationError("City name should contain only alphabetical characters")
        
        if icao_code and len(icao_code) != 4:
            raise serializers.ValidationError("The ICAO code must be exactly 4 characters long.")
        
        return attrs

    
# Aircraft Serializer
class AircraftSerializers(serializers.ModelSerializer):

    class Meta:
        model = Aircraft
        fields = ["id", "Aircraft_Model","Serialnumber","Manufacturer"]
        read_only_fields = ["id", ]



# Flight Serializer
class FlightSerializers(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = ["id", "Flight","Flight_Id","Flight_name","Departure_airport","Arrival_airport","Departure_Datetime","Arrival_Datetime"]
        read_only_fields = ["id", ]

    def validate(self, attrs):
        Departure_Datetime = attrs.get('Departure_Datetime')
        Arrival_Datetime = attrs.get('Arrival_Datetime')
        Flight_Id = attrs.get('Flight_Id')
        Flight_name = attrs.get('Flight_name')
        Departure_airport = attrs.get('Departure_airport')
        Arrival_airport = attrs.get('Arrival_airport')

        if Departure_Datetime <= timezone.now():
            raise serializers.ValidationError("Departure datetime should be in the future")
        
        if Departure_Datetime >= Arrival_Datetime:
            raise serializers.ValidationError("Arrival datetime should be after departure datetime")
        
        if Departure_Datetime == Arrival_Datetime:
            raise serializers.ValidationError("Departure and Arrival Airport should not be same")
        
        if Flight.objects.filter(Flight_Id=attrs['Flight_Id']).exists():
            raise serializers.ValidationError("Flight with this ID already exists.")

        if Flight.objects.filter(Flight_name=attrs['Flight_name']).exists():
            raise serializers.ValidationError("Flight with this name already exists.")
            
        if Flight.objects.filter(Q(Flight=Flight)):

            if not Departure_Datetime and not Arrival_Datetime:
                pass
            else:
                aparture_time = Flight.objects.filter(Q(Flight=Flight) & Q(is_active=True)).aggregate(apartime=Max('Arrival_Datetime'))
                print(aparture_time)

                Apartime = aparture_time['apartime'] + timedelta(minutes=20)
                print(Apartime)

                if Departure_Datetime < Apartime:
                    raise serializers.ValidationError({
                        "flight_time": "You should enter departure time after 20 Minutes's arrive time."
                    })

                dep_center = Flight.objects.filter(Q(Flight=Flight) & Q(
                    Aparture_Flight_Time=aparture_time['apartime'])).values('Arrival_airport')
                print(dep_center)

                if int(Departure_airport.id) != dep_center[0]['Arrival_airport']:
                    raise serializers.ValidationError({
                        "flight_arrival": "This flight should be departure from arrival destination."})

        return attrs

        # return attrs
    

     
#####################




