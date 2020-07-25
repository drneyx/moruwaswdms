
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from  PIL import Image


# Create your models here.


#class Position(models.Model):
 #   title = models.CharField(max_length=50)

  #  def __str__(self):
   #     return self.title
    

class Employee(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=100)
	emp_code = models.CharField(max_length=42)
	mobile = models.CharField(max_length=15)
	position = models.CharField(max_length =54)
	profile_pic = models.ImageField(default="try.svg",null=True, blank=True)

	def __str__(self):
		return self.fullname


	#def save(self):
	#	super().save()
	#	img = Image.open(self.profile_pic.path)


	#	if img.height > 300 or img.width > 300:
	#		output_size = (300, 300)
	#		img.thumbnail(output_size)
	#		img.save(self.profile_pic.path)
 
   # position = models.ForeignKey(Position,on_delete=models.CASCADE) 



class TechDetails(models.Model):
	name = models.CharField(max_length=30, null = True)
	phone = models.CharField(max_length=15, null=True) 
	STATUS = (
		      ('Available','Available'),
		      ('Not Available','Not Available')
		      )

	date_created = models.DateTimeField(auto_now_add=True,null=True)
	status = models.CharField(max_length=200,null=True,choices=STATUS)
	task = models.CharField(max_length=500, null=True)


	def __str__(self):
		return self.name



class AssignTech(models.Model):
	techDetails = models.ForeignKey(TechDetails, null=True, on_delete= models.SET_NULL)
	employee = models.ManyToManyField(Employee)
	message = models.CharField(max_length=200,null=True)
	date_created = models.DateTimeField(auto_now_add=True,null=True)


	def __str__(self):
		return self.techDetails



class SensorData(models.Model):
	date_created = models.DateTimeField(auto_now_add=True,null=True)
	height = models.CharField(max_length=21)
	status = models.BooleanField(max_length=4)
	rate = models.FloatField(max_length=12)
	volume = models.FloatField(max_length=32)


	def __str__(self):
		return self.height



    


class BlockDetails(models.Model):
	block_name = models.CharField(max_length=50)
	block_number = models.CharField(max_length=89)
	block_meter_reader =models.CharField(max_length=60)
	block_total_customers = models.IntegerField()
	block_av_usage = models.FloatField(max_length=20)



class Meta:
	get_latest_by = ['height']
    
