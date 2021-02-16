import django_filters
from django_filters import DateTimeFilter,NumberFilter,CharFilter
from .models import *

class RideFilter(django_filters.FilterSet):
    class Meta:
        model =Ride
        fields = ['status']

class SharerFilter(django_filters.FilterSet):
    start_time = DateTimeFilter(field_name='arrival_time', lookup_expr='gte')
    end_time = DateTimeFilter(field_name='arrival_time', lookup_expr='lte')
    sharer_number = NumberFilter(field_name='max_sharer_number',lookup_expr='gte')
    destination = CharFilter(field_name='destination',lookup_expr = 'iexact')
    special_request = CharFilter(field_name='special_request',lookup_expr = 'iexact')
    class Meta:
       model =Ride
       fields = ['vehicle_type','destination','special_request']


class driverRideFilter(django_filters.FilterSet):
    start_time = DateTimeFilter(field_name='arrival_time', lookup_expr='gte')
    end_time = DateTimeFilter(field_name='arrival_time', lookup_expr='lte')
    destination = CharFilter(field_name='destination',lookup_expr = 'iexact')
    special_request = CharFilter(field_name='special_request',lookup_expr = 'iexact')
    class Meta:
       model =Ride
       fields = ['vehicle_type','destination','special_request']
    
