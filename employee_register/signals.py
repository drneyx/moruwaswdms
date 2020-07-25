from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Employee


def employee_profile(sender, instance,create,**kwargs):
	if created:
		group = Group.objects.get(name='Technicians')
		instance.groups.add(group)


		Employee.objects.













	