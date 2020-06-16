from .models import Temp
from rest_framework.serializers import ModelSerializer

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Temp
        fields='__all__'

        depth=1