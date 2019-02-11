from django.contrib import admin

# Register your models here
from .models import User_Details, Trip


admin.site.register(User_Details)
admin.site.register(Trip)
