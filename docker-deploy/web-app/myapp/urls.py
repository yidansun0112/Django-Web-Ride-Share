from  django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('vehicle_info/<str:pk>/',views.vehicleInfoPage,name="vehicle_info"),
    path('become_driver/<str:pk>/',views.becomeDriverPage,name="become_driver"),
    path('get_ride/<str:pk>/',views.getRidePage,name="get_ride"),
    path('driver_ride/<str:pk>/',views.driverRidePage,name="driver_ride"),
    path('confirm_ride/<str:user_pk>/<str:ride_pk>/',views.confirmPage,name="confirm_ride"),
    path('complete_ride/<str:pk>/',views.completePage,name="complete_ride"),
    path('create_ride/<str:pk>/', views.createRide, name="create_ride"),
    path('update_ride/<str:pk>/', views.updateRide, name="update_ride"),
    path('no_update/', views.noUpdate, name="no_update"),
    path('owner_rides/<str:pk>/', views.searchOwnerRide,name="search_owner_ride"),
    path('sharer_rides/<str:pk>/', views.searchSharerRide,name="search_sharer_ride"),
    path('join_rides/<str:pk>/', views.SharerJoinRide, name="join_rides"),
    path('confirm_join/<str:user_pk>/<str:ride_pk>/<str:num>/', views.Join, name="confirm_join"),
    path('already_driver', views.alreadyDriver, name="already_driver"),
    path('not_driver', views.notDriver, name="not_driver"),
    path('cancel_driver/<str:pk>/', views.cancelDriverPage, name="cancel_driver"),
]
