from django.db import models

# Create your models here.
class Aircraft(models.Model):
    Aircraft_Model = models.CharField(max_length = 50)
    Serialnumber = models.CharField(max_length=50,unique=True)
    Manufacturer = models.CharField(max_length = 50)


    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # deleted_on = models.CharField(auto_add = True)

    def __str__(self):
        return f"{self.Aircraft_Model} "


class Airport(models.Model):
    Airport_Name = models.CharField(max_length = 200,unique = True)
    Country = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    ICAO_Code = models.CharField(max_length = 4 ,unique = True)
	

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
	
    def __str__(self):
        return f"{self.ICAO_Code}"


class Flight(models.Model):
    # aircraft = models.ForeignKey(Aircraft,on_delete=models.CASCADE)
    Flight = models.ForeignKey(Aircraft,on_delete=models.CASCADE)
    Flight_Id = models.CharField(max_length = 200,unique = True)
    Flight_name =models.CharField(max_length = 200,unique = True)
    Departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    Arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    Departure_Datetime = models.DateTimeField()
    Arrival_Datetime = models.DateTimeField()
	

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # deleted_on = models.CharField(auto_add = True)

    def __str__(self):
        return f"{self.Flight_Id}"
    



