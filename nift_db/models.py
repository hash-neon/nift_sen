from django.db import models

# Create your models here.
class User(models.Model):
	SEX_CHOICES = (
		('M','Male'),
		('F','Female'),
	)

	STATUS_CHOICES = (
		('Married',''),
		('Unmarried',''),
	)

	first_name 	= models.CharField(max_length=100)
	last_name  	= models.CharField(max_length=100)
	login_name 	= models.CharField(max_length=100, unique=True) 
      	sex        	= models.CharField(max_length=1 ,choices=SEX_CHOICES)
	password   	= models.CharField(max_length=100)
	email_add  	= models.EmailField(max_length=100)
	dob 	   	= models.DateField()
	phone_no   	= models.SmallIntegerField()
	user_id    	= models.CharField(max_length=100, primary_key=True)	
	marital_status  = models.CharField(max_length=100, choices=STATUS_CHOICES)

class Attendance(models.Model):
	date 		= models.DateField(auto_now=True)
	present 	= models.BooleanField()
	user_id 	= models.ForeignKey(User)
	user_id.primary_key = True
