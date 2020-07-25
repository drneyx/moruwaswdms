from employee_register.models import SensorData
from rest_framework.serializers import ModelSerializer


class SensorDataSerializer(ModelSerializer):
	class Meta:
		model = SensorData
		fields = '__all__'