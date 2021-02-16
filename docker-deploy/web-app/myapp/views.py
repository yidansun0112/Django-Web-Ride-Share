from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.template import loader
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

from django.contrib import messages
from .forms import *
from .models import *
from .filters import *


def registerPage(request):
    form = CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
            
    context={'form':form}
    return render(request,'myapp/register.html',context)
    
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:        
        if request.method == 'POST':
            username = request.POST.get('username')
       	    password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context={}                                              
        return render(request,'myapp/login.html',context) 

def logoutUser(request):
	logout(request)
	return redirect('login')


def home(request):
    context={}
    return render(request,'myapp/index.html',context)

def becomeDriverPage(request,pk):
    owner=User.objects.get(id=pk)
    if owner.is_driver==False:
        form=vehicleInfoForm()
        if request.method=='POST':
            vehicle=Vehicle.objects.create(owner=owner)
            form=vehicleInfoForm(request.POST,instance=vehicle)
            if form.is_valid():
                User.objects.filter(id=pk).update(is_driver=True)
                print(owner.is_driver)
                form.save()
                return redirect('home')

        context={'form':form}
        return render(request,'myapp/become_driver.html',context)

    else:
        return redirect('already_driver')

    
        

def vehicleInfoPage(request,pk):
    owner=User.objects.get(id=pk)
    if owner.is_driver==True:
        vehicle=Vehicle.objects.get(owner=owner)
        form =vehicleInfoForm(instance=vehicle)
        if request.method=='POST':
            form=vehicleInfoForm(request.POST,instance=vehicle)
            if form.is_valid():
                form.save()              
                return redirect('home')
            else:
                print("form is not valid")
        context={'form':form}
        return render(request,'myapp/vehicle_info.html',context)

    else:
        return redirect('not_driver')
        
    
def getRidePage(request,pk):
    owner=User.objects.get(id=pk)
    if owner.is_driver==False:
        return redirect('not_driver')
    
    vehicle=Vehicle.objects.get(owner=owner)
    
    if vehicle==None:
        return redirect('become_driver',pk=owner.id)

    rides=Ride.objects.filter(status="Open")|Ride.objects.filter(status="Sharer_joined")
    rides=rides.filter(number_of_passengers__lte=vehicle.max_number_passengers).exclude(owner=owner)
    rides_type=rides.filter(vehicle_type=None)|rides.filter(vehicle_type=vehicle.vehicle_type)
    rides_request=rides.filter(special_request=None)|rides.filter(special_request=vehicle.special_request)
    rides=rides_type&rides_request
    myFilter = driverRideFilter(request.GET, queryset=rides)
    rides=myFilter.qs
    context={'rides':rides,'myFilter': myFilter}
    return render(request,'myapp/get_ride.html',context)

def driverRidePage(request,pk):
    driver=User.objects.get(id=pk)
    if driver.is_driver==False:
        return redirect('not_driver')
    
    rides=Ride.objects.filter(driver=driver).filter(status="Confirmed")
   
    
    context={'rides':rides}
    return render(request,'myapp/driver_ride.html',context)
    
def confirmPage(request,user_pk,ride_pk):
    ride = Ride.objects.get(id=ride_pk)
    driver=User.objects.get(id=user_pk)

    if driver.is_driver==False:
        return redirect('not_driver')

    vehicle=Vehicle.objects.get(owner=driver)
    
    if request.method == "POST":
        Ride.objects.filter(id=ride_pk).update(driver=driver,status="Confirmed",vehicle_type=vehicle.vehicle_type)
        send_mail(
            'Confirm email',
            'Hello, your ride has been confirmed. The driver will come soon! Have a good journey!',
            'ece568server@163.com',
            [ride.owner.email],
            fail_silently=False,
        )
        for sharer in ride.sharer.all():
            send_mail(
                'Confirm email',
                'Hello, your ride has been confirmed. The driver will come soon! Have a good journey!',
                'ece568server@163.com',
                [sharer.email],
                fail_silently=False,
            )
        
        return redirect('home')

    context = {'ride':ride}
    return render(request, 'myapp/confirm_ride.html', context)

def completePage(request,pk):
    ride = Ride.objects.get(id=pk)   
    if request.method == "POST":
        Ride.objects.filter(id=pk).update(status="Complete")
        return redirect('home')

    context = {'ride':ride}
    return render(request, 'myapp/complete_ride.html', context)

def cancelDriverPage(request,pk):
    driver = User.objects.get(id=pk)
    if driver.is_driver==False:
        return redirect('not_driver')    
    if request.method == "POST":
        User.objects.filter(id=pk).update(is_driver=False)
        Vehicle.objects.filter(owner=driver).delete()
        return redirect('home')

    context = {}
    return render(request, 'myapp/cancel_driver.html', context)


def alreadyDriver(request):
    context={}
    return render(request,'myapp/already_driver.html',context)

def notDriver(request):
    context={}
    return render(request,'myapp/not_driver.html',context)

def createRide(request, pk):
    owner = User.objects.get(id=pk)
    ride = Ride.objects.create(owner=owner,status='Open')
    print("create a ride")
    print('Printing POST:', request.POST)
    form = RideForm(request.POST,instance=ride)
    if(form.is_valid()):
        if((form['shared_or_not'].data == 'Yes' and form['max_sharer_number'].data!= '')or (form['shared_or_not'].data == 'No' and form['max_sharer_number'].data== '')):
            form.save()
            return redirect('home')
        else:
            ride.delete()
    else:
        ride.delete()
    
    context = {'form':form}
    return render(request, 'myapp/ride_form.html', context)

def updateRide(request,pk):
    ride = Ride.objects.get(id=pk)
    
    if ride.status == 'Open':
        form =RideForm(instance=ride)
        if request.method=='POST':
            form = RideForm(request.POST, instance=ride)
            if(form.is_valid()):
                form.save()
                return redirect('home')
            else:
                print('not valid form')
        context = {'form':form}
        return render(request, 'myapp/ride_form.html', context)
    else:
        return redirect('no_update')
    
def noUpdate(request):
    context={}
    return render(request, 'myapp/no_update.html', context)
        
        
def searchOwnerRide(request,pk):
    user = User.objects.get(id=pk)
    ride_users = Ride.objects.filter(owner = user)
    myFilter = RideFilter(request.GET, queryset=ride_users)
    ride_users = myFilter.qs
    context = {'ride_users': ride_users, 'myFilter': myFilter}
    return render(request, 'myapp/my_rides.html',context)

def searchSharerRide(request,pk):
    user = User.objects.get(id=pk)
    ride_users = Ride.objects.filter(sharer = user)
    myFilter = RideFilter(request.GET, queryset=ride_users)
    ride_users = myFilter.qs
    context = {'ride_users': ride_users, 'myFilter': myFilter}
    return render(request, 'myapp/my_rides.html',context)

def SharerJoinRide(request,pk):
    user = User.objects.get(id=pk) 
    my_rides = Ride.objects.filter(status ='Open').exclude(owner=user)
    myFilter = SharerFilter(request.GET, queryset=my_rides)
    number=myFilter.form['sharer_number'].data
    #print(number)
    my_rides = myFilter.qs
    #rides = Ride.objects.filter(shared_or_not = 'Yes', max_sharer_number= None)
    #my_rides =rides | my_rides
    context = {'my_rides': my_rides, 'myFilter': myFilter,'number':number}
    return render(request, 'myapp/join_rides.html',context)

def Join(request,user_pk, ride_pk,num):
    user = User.objects.get(id=user_pk)
    ride = Ride.objects.get(id=ride_pk)
    ride.sharer.add(user)
    print(num)
    print(type(num))
    number_of_passengers=ride.number_of_passengers
    #number=string.atoi(num)
    Ride.objects.filter(id=ride_pk).update(status='Sharer_joined',number_of_passengers=number_of_passengers+int(num))
    context = {}
    return render(request, 'myapp/join.html',context)
