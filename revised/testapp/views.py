from .serializer import EmployeeSerializer
from .models import Temp
from datetime import date
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class EmployeeCURDCBV(ModelViewSet):
    queryset = Temp.objects.all()
    serializer_class = EmployeeSerializer




class TempDetailView(ModelViewSet):

        queryset=Temp.objects.filter(temp_reading__gte=100)&Temp.objects.filter(pub_date__startswith=date.today())
        serializer_class = EmployeeSerializer

class dateDetailView(ModelViewSet):
        queryset = Temp.objects.filter(pub_date=date.today())
        serializer_class = EmployeeSerializer

