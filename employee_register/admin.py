from django.contrib import admin

# Register your models here.

from .models import AssignTech,Employee,SensorData,TechDetails,BlockDetails


admin.site.register(AssignTech)
admin.site.register(Employee)
admin.site.register(SensorData)
admin.site.register(TechDetails)
admin.site.register(BlockDetails)



