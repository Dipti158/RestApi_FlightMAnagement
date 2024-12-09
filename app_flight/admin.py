from django.contrib import admin
from .models import Aircraft,Airport,Flight

# Register your models here.


@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ["id","Aircraft_Model", "Serialnumber", "Manufacturer"]

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ["id","Airport_Name", "Country", "City","ICAO_Code"]

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ["id","Flight", "Flight_Id", "Flight_name","Departure_airport","Arrival_airport","Departure_Datetime","Arrival_Datetime"]