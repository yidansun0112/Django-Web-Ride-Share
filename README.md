# README

* Author: [Yidan Sun ys303] [Denise Liu xl340]
* Course: [ECE568]
* Term: [2021spring]
* Professor: [Brian Rogers]



### **You need to access http://0.0.0.0:8000/myapp/register/ to register at first!!!**



## Structure of Our Web

### Passenger Part

There are actually 5 functionalities for the passenger:  become a driver, create a ride, select and view the rides, update the rides and join a ride.

#### Become Driver

From this page, a user could become a driver by submitting vehicle info. Among the blanks, `vehicle type`, `license plate number` and `max number passengers` are required and special request is optional.

#### **Create a ride**

For a passenger, he/she can create a ride (then become the owner of the ride) by type in the `destination`, `arrival time`, if the ride can be `shared or not`, and `number of passengers` in their party. When the owner set this ride to be shared, he/she must specify the `max number of sharers` that he/she allows to join the ride. If the ride is set to be not shared, the owner can not fill in the blank of max sharer number. If the owner disobeys these two rules, they could not create a ride successfully. Besides, the owner can choose to input the `vehicle type` and `special request` (these two are optional). If the user doesn't fill out all the obligatory ones or the formats of the input are wrong, the ride can't be created successfully and this form can't be submitted. Once the ride is successfully created, the web page would automatically jumps to home page.

#### **View and update rides**

A passenger can also view all the rides that relate to him/her, either he/she owns or shares. Passengers can also make a update on all the open rides that they own or share. Also, the sign of successfully update the info of rides is automatically jumps back to the home page. There are actually 4 kinds of status: `open`, `sharer_joined`, `confirm` and `complete`. Only the open rides can be updated. For those rides that are not open, by clicking on the  update button, it would jump to a page that tell the passengers that they are not allowed to update.

#### **Join a ride**

When a passenger wants to join a ride, he/she can filter rides that are currently open by setting the `arrival time window`, `destination` and `number of passengers in his/her party` along with `special request`. Only the rides whose status is open and the owner allows sharing can be in the query set. After finding the ride the passenger wants, he/she can click on the join button and join that ride. Then the joined ride's status would become sharer_joined, which can no longer be joined by other people. What's more, the number of passengers of that ride would plus the number of people from the sharer party.



### Driver Part

There are four functional pages for the driver part.

#### Vehicle Info

A driver could view and edit his/her verhilce information in this page. 

Vehicle Info contains : `Vehilce type`, `License plate number`,`Max number passengers allowed` ,`special request`.

#### Get Ride

A driver could get rides in this page. This page will automatically search any ride meet this driver's vehicle info.

* number of passengers of this ride need to less than or equal to max number of passed
* Vehicle type of this ride need to be none or equal to this driver's vehicle type
* Special request of this ride need to be none or equal to this driver's special request

A driver could also search among these rides by specifying `vehicle type`, `Destination`, `Arrival window` and `special request`.

For any ride, the driver could click the confirm button to get it.

#### My Ride

This page lists all confirmed rides from this driver. For any ride, the driver could click the complete button to complete it.

#### Not be Driver

From this page, a driver could decide no longer to be a driver. After clicking the `Yes` button, this user will no longer be a driver and his/her vehicle info will be deleted from the database.



### Sign out

Sign out button is on the right up corner from the home page. By clicking this button, you will logout and jump back the login page.



## Resources Referenced

#### Django Tutorial

https://docs.djangoproject.com/en/3.1/intro/tutorial01/

#### YouTube Tutorial

https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO

#### Bootstrap Dashboard

https://getbootstrap.com/docs/5.0/examples/dashboard/