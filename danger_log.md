# Danger Log



#### User can access any functionality page without any identity check. 

As our url path for the functionalities are made up by some key words and user_id/ ride_id. That means by changing the id in the url path, a user can actually view or even edit any data that stored in the database, no matter if that relates himself/herself. To avoid that, we may should add constraints on some page that they can only be accessed after logging in. Also, we should make other permission check to make sure one login user can not access other data.



#### User email account may be in valid.

When a user tries to register, his/her email account may not be valid. This would make the web can't remind him/her that rides have been confirmed. To eliminate it, We probably can check the validity of the user email when a user account is being created instead of just taking whatever the user inputs.



#### User names may be the same

When a user tries to register, his/her user name may be the same with the user account that already exists in our database. Since when user tries to login, he/she only needs to type in the user name and password. There might be unexpected errors when 2 same name user tries to login. To solve, when a user tries to register, we may also add some user name checking, to make sure there are no objects that have the same user name in the database.



#### User password may be too easy

When a user tries to register, his/her password might be too easy which could have the risking of being hacked. To reduce the impact of that danger, we could ask a user to use some complex combinations of number, letters etc. For the passwords that are made up only by short consecutive numbers, our web shouldn't allow the registration and asks the use to type in a more complex one.



#### Didn't check the validity of license plate number

When a user tried to become a driver, he/she could achieve this by filling out vehicle information, one of those is `license plate number`. In real world, the license plate number of a vehicle should be valid, which means that it must be officially registered, so that the platform could have better supervision on drivers. However on our web, we just accept any string the user type in. In other words, we just allowed anyone to be a driver. This could cause huge danger problem.

To eliminate this, we think we may need get data from relative department to investigate validity of the vehicle and the driver. And let the user to upload some official documents to prove the validity of the information. 



#### Arrival time of ride can be any date time without checking later than the create time

When a user create a ride, he/she needs to fill out some information. There is one named arrival time, which is the expected arrival time specified by the user. We just let the user type any time he/she wants. Therefore, this time could be earlier than the current create time. This should be banned because it is impossible for time to reverse. We could add a constraint of time at this page to reduce this danger.



#### Driver can hold multiple rides whose driving period overlap

Driver could hold multiples ride at the same time. This may cause problem when two rides' arrival time are too close. In this circumstance, it will be impossible for a driver to accomplish these rides all on time. Our web should be able to forbid a driver to get rides that may conflict with each other. To achieve this, we may need information like how long it usually takes from one place to another and do complicated computation to decide whether two rides will have overlap.