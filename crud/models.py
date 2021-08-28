from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)

    def __str__(self):
        return self.firstname + " " + self.lastname

class Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=40)
    qty = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    c_name = models.CharField(max_length=40)
    image = models.CharField(max_length=40)
    img = models.CharField(max_length=40)
    picture = models.CharField(max_length=40)
    pic = models.CharField(max_length=40)
    pica = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    category = models.CharField(max_length=40)
    engine = models.CharField(max_length=40)
    displacement = models.CharField(max_length=40)
    power = models.CharField(max_length=40)
    drivetrain = models.CharField(max_length=40)
    fuel_tank_capacity = models.CharField(max_length=40)
    airbags = models.CharField(max_length=40)
	
    def __str__(self):
        return self.name + " " + self.price
		
class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    mobile_number = models.CharField(max_length=40)
    email_id = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
  	
    def __str__(self):
        return self.username + " " + self.password

class Cart(models.Model):
    cust_id = models.CharField(max_length=40)
    pid = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    c_name = models.CharField(max_length=40)
    image = models.CharField(max_length=40)
    image = models.CharField(max_length=40)
    img = models.CharField(max_length=40)
    picture = models.CharField(max_length=40)
    pic = models.CharField(max_length=40)
    pica = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    engine = models.CharField(max_length=40)
    displacement = models.CharField(max_length=40)
    power = models.CharField(max_length=40)
    drivetrain = models.CharField(max_length=40)
    fuel_tank_capacity = models.CharField(max_length=40)
    airbags = models.CharField(max_length=40)
    dt = models.CharField(max_length=40)
	
class Show_cars(models.Model):
    pid = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    c_name = models.CharField(max_length=40)
    image = models.CharField(max_length=40)
    img = models.CharField(max_length=40)
    picture = models.CharField(max_length=40)
    pic = models.CharField(max_length=40)
    pica = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    engine = models.CharField(max_length=40)
    displacement = models.CharField(max_length=40)
    power = models.CharField(max_length=40)
    drivetrain = models.CharField(max_length=40)
    fuel_tank_capacity = models.CharField(max_length=40)
    airbags = models.CharField(max_length=40)
    dt = models.CharField(max_length=40)
	
class Bill(models.Model):
    pid = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    product = models.CharField(max_length=40)
    price = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    dt = models.CharField(max_length=40)
	
    def __str__(self):
        return self.username + " " + self.price

