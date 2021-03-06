from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Nift_User(models.Model):
	SEX_CHOICES = (
		('M','Male'),
		('F','Female'),
	)

	STATUS_CHOICES = (
		('M','Married'),
		('U','Unmarried'),
	)

	login_name 	= models.OneToOneField(User) 
      	sex        	= models.CharField(max_length=1, choices=SEX_CHOICES)
	dob 	   	= models.DateField()
	phone_no   	= models.CharField(max_length=15)
	user_id    	= models.CharField(max_length=20, primary_key=True)	
	marital_status  = models.CharField(max_length=1, choices=STATUS_CHOICES)
	perm_street 	= models.CharField(max_length=200)
	perm_zip 	= models.SmallIntegerField()
	perm_state 	= models.CharField(max_length=50)

class Profile(models.Model):
	DESIGNATION_CHOICES = (
		('1','Professor'),
		('2','Assistant Professor'),
		('3','Associate Professor'),
		('4','Senior Professor'),
		('5','Director'),
		('6','Assistant'),
		('7','Centre Coordinator'),
		('8','Director General'),
	)

	CENTRE_CHOICES = (
		('1','Bhopal'),
		('2','Bhuwaneshwar'),
		('3','Bengaluru'),
		('4','Delhi'),
		('5','Kangra'),
		('6','Chennai'),
		('7','Kolkatta'),
		('8','Mumbai'),
		('9','Gandhinagar'),
		('10','Raebareli'),
		('11','Jodhpur'),
		('12','Patna'),
		('13','Hyderabad'),
		('14','Shillong'),
	)

	join_date 	= models.DateField()
	designation 	= models.CharField(max_length=1, choices=DESIGNATION_CHOICES)
#	department 	= models.CharField(max_length..........)
	centre 		= models.CharField(max_length=2, choices=CENTRE_CHOICES)
	room_no 	= models.CharField(max_length=10)
	past_positions 	= models.CharField(max_length=150, blank=True)
	experience 	= models.SmallIntegerField(null=True)
	expertise 	= models.CharField(max_length=150, blank=True)
	image 		= models.ImageField(upload_to='/images/%Y/%m/%d')
	user_id 	= models.ForeignKey(Nift_User, primary_key=True)

class Attendance(models.Model):
	date 		= models.DateField(auto_now=True)
	present 	= models.BooleanField()
	user_id 	= models.ForeignKey(Nift_User)
	user_id.primary_key = True

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
	cen_dep_id 	= models.AutoField(primary_key=True)

class Offered(models.Model):
	sem_id 		= models.ForeignKey(Sem_Info)
	course_id 	= models.ForeignKey(Course)
	cen_dep_id 	= models.ForeignKey(Cen_Dep_Info)
	every_id 	= models.AutoField(primary_key=True)
	user_id         = models.ForeignKey(Nift_User)

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

	study_type 	= models.CharField(max_length=1, choices=STUDY_CHOICES)
	detail_type 	= models.CharField(max_length=1, choices=TYPE_CHOICES, blank=True)
	teaching_id 	= models.AutoField(primary_key=True)
	hours 		= models.SmallIntegerField()
	every_id 	= models.ForeignKey(Offered)
	user_id 	= models.ForeignKey(Nift_User)

class Feedback(models.Model):
	WEEK_CHOICES = (
		('1','First'),
		('2','Second'),
		('3','Third'),
		('4','Forth'),
	)

	week_no 	= models.CharField(max_length=1, choices=WEEK_CHOICES)
	avg_content_rat = models.SmallIntegerField(null=True)
	avg_present_rat = models.SmallIntegerField(null=True)
	feedback_id 	= models.AutoField(primary_key=True)
	every_id        = models.ForeignKey(Offered)

class Leave_Info(models.Model):
	LEAVE_CHOICES = (
		('1','Earned'),
		('2','Casual'),
		('3','Restricted'),
		('4','Hospital'),
		('5','Maternity'),
	)

	leave_type 	= models.CharField(max_length=1, choices=LEAVE_CHOICES)
	start_date 	= models.DateField()
	reason 		= models.CharField(max_length=1000)
	no_of_days 	= models.SmallIntegerField()
	approved 	= models.BooleanField()
	days_left 	= models.SmallIntegerField()
	user_id 	= models.ForeignKey(Nift_User)
	leave_id 	= models.AutoField(primary_key=True)

class Leave_Extension_Info(models.Model):
	last_leave_id 	= models.ForeignKey(Leave_Info)
	reason 		= models.CharField(max_length=1000)
	approved 	= models.BooleanField()
	no_of_days      = models.SmallIntegerField()
	eleave_id 	= models.AutoField(primary_key=True)
