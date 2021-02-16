from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *


class CreateUserForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = User
		fields = ['username', 'email', 'password1', 'password2']

                
        
class RideForm(ModelForm):
        class Meta:
                model =Ride
                fields = ['destination','arrival_time','shared_or_not','max_sharer_number','number_of_passengers','vehicle_type','special_request']
    


  
class vehicleInfoForm(ModelForm):
        class Meta:
                model=Vehicle
                fields=['vehicle_type','license_plate_number','max_number_passengers', 'special_request']
         
