from django.db import models


class User_Details(models.Model):
    user_id = models.IntegerField( primary_key=True)
    username = models.CharField(max_length=255, )
    name = models.CharField(max_length=255, )
    password = models.CharField(max_length=255, )

    def __str__(self):
        return self.name

class Trip(models.Model):
    trip_id = models.IntegerField( primary_key=True)
    driver_name = models.CharField(max_length=255, )
    reg_number = models.CharField(max_length=255, )
    opening_milage = models.IntegerField()
    closing_milage = models.IntegerField()
    destination = models.CharField( max_length=255)
    comments = models.TextField( max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.trip_id