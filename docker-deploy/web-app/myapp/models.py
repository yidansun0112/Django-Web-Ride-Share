from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(User) :
   # vehicle=models.OneToOneField(Vehicle,on_delete=model.CASCADE,null=True,blank=True)
    is_driver = models.BooleanField(default = False)
    #is_driving = models.BooleanField(default = False)

class Vehicle(models.Model):
    owner=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    TYPE = [('Ecnomic', 'Ecnomic' ),
            ('Comfortable', 'Comfortable'),
            ('Luxury', 'Luxury')]
    vehicle_type = models.CharField(max_length=20, choices= TYPE,null=True)
    license_plate_number = models.CharField(max_length=200,null=True)
    max_number_passengers = models.IntegerField(null=True)
    special_request = models.CharField(max_length=200, blank =True,null=True)
    
class Ride(models.Model):
    driver =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='driver_user',null=True,blank=True)
    sharer = models.ManyToManyField(User,blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner_user',null=True)
    destination = models.CharField(max_length=200,null=True)
    arrival_time = models.DateTimeField(null=True)
    shared_type = [('Yes', 'Yes'),('No','No')]
    shared_or_not = models.CharField(max_length = 5, choices = shared_type,null=True)
    max_sharer_number = models.IntegerField(blank=True, null=True)
    number_of_passengers = models.IntegerField(null=True)
    Vehicle_TYPE = [('Ecnomic', 'Ecnomic' ),
            ('Comfortable', 'Comfortable'),
            ('Luxury', 'Luxury')]
    vehicle_type = models.CharField(max_length=20, choices= Vehicle_TYPE, blank = True,null=True)
    special_request = models.CharField(max_length=200, blank =True,null=True)
    TYPE = [('Open', 'Open' ),
             ('Sharer_joined', 'Sharer_joined'),
             ('Confirmed', 'Confirmed'),
             ('Complete', 'Complete') ]
    status = models.CharField(max_length=20, choices=TYPE,null=True, default='Open')
    

    
