from django.db import models

# Create your models here.
class User(models.Model):
	SEX_CHOICES = (
		('M','Male'),
		('F','Female'),
	)

	STATUS_CHOICES = (
		('M','Married'),
		('U','Unmarried'),
	)

	first_name 	= models.CharField(max_length=100)
	last_name  	= models.CharField(max_length=100)
	login_name 	= models.CharField(max_length=100, unique=True) 
      	sex        	= models.CharField(max_length=1, choices=SEX_CHOICES)
	password   	= models.CharField(max_length=100)
	email_add  	= models.EmailField(max_length=100)
	dob 	   	= models.DateField()
	phone_no   	= models.SmallIntegerField()
	user_id    	= models.CharField(max_length=20, primary_key=True)	
	marital_status  = models.CharField(max_length=1, choices=STATUS_CHOICES)

class Attendance(models.Model):
	date 		= models.DateField(auto_now=True)
	present 	= models.BooleanField()
	user_id 	= models.ForeignKey(User)
	user_id.primary_key = True

class Address(models.Model):
	user_id         = models.ForeignKey(User, primary_key=True)
	perm_street 	= models.CharField(max_length=200)
	perm_zip 	= models.SmallIntegerField()
	perm_state 	= models.CharField(max_length=50)
	temp_street     = models.CharField(max_length=200)                                  
	temp_zip        = models.SmallIntegerField()
        temp_state  	= models.CharField(max_length=50)

class Sem_Info(models.Model):
	TERM_CHOICES = (
		('1','Winter'),
		('2','Autumn'),
        )

	term 		= models.CharField(max_length=1, choices=TERM_CHOICES)
	year 		= models.CharField(max_length=4)
	sem_id 		= models.AutoField(primary_key=True)

class Course(models.Model):
	course_name 	= models.CharField(max_length=50)
	course_id 	= models.CharField(max_length=20, primary_key=True)

class Cen_Dep_Info(models.Model):
	centre_name 	= models.CharField(max_length=50)
	department_name = models.CharField(max_length=50)
	cen_dep_info 	= models.AutoField(primary_key=True)

class Offered(models.Model):
	sem_id 		= models.ForeignKey(Sem_Info)
	course_id 	= models.ForeignKey(Course)
	cen_dep_info 	= models.ForeignKey(Cen_Dep_Info)
	user_id 	= models.ForeignKey(User)

class Teaching(models.Model):
	STUDY_CHOICES = (
	       	('D','Direct'),
               	('I','InDirect'),
		('A','Audit'),
        )

	TYPE_CHOICES = (
		('1','CoTeaching'),
		('2','IndividualTeaching'),
		('3','OtherCentre'),
		('4','GP'),
		('5','DC'),
		('6','ResearchPaper'),
		('7','ITP'),
		('8','CraftCluster'),
	)

	sem_id 		= models.ForeignKey(Sem_Info)
	course_id 	= models.ForeignKey(Course)
	user_id 	= models.ForeignKey(User)
	study_type 	= models.CharField(max_length=1, choices=STUDY_CHOICES)
	detail_type 	= models.CharField(max_length=1, choices=TYPE_CHOICES)
	teaching_id 	= models.AutoField(primary_key=True)
