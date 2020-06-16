from django.contrib import admin
from .models import Temp,Temp_dev,Device
# Register your models here.
admin.site.register(Temp_dev)
admin.site.register(Temp)
admin.site.register(Device)