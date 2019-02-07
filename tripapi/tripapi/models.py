from django.db import models


class Users(models.Model):
    user_id = models.IntegerField(null=False, primary_key=True)
    username = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)

    def __str__(self):
        return(self.user_id, self.username, self.name, self.password)

class Trip(models.Model):
    trip_id = models.IntegerField(null=False, primary_key=True)
    driver_name = models.CharField(max_length=255, null=False)
    reg_number = models.CharField(max_length=255, null=False)
    opening_milage = models.IntegerField(null=False)
    closing_milage = models.IntegerField(null=False)
    destination = models.CharField(null=False, max_length=255)
    comments = models.TextField(null=True, max_length=500)
    date = models.DateField(null=False)

    def __str__(self):
        return(self.trip_id, self.driver_name, self.reg_number, self.opening_milage,
        self.closing_milage, self.destination, self.comments, self.date)
