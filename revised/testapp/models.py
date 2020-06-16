from django.db import models




class Device(models.Model):
    device_name = models.CharField(max_length=30,null=True,blank=True,default='nothing')
    def __str__(self):
        return self.device_name

class Temp_dev(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.TextField(max_length=100)



    def __str__(self):
        return self.first_name



class Temp(models.Model):
    pub_date = models.DateField(auto_now=True)
    temp_reading=models.IntegerField()
    Employee_id= models.ForeignKey(Temp_dev, on_delete=models.CASCADE)
    Device_id = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
         return "%d " % (self.temp_reading)

    class Meta:
        ordering = ['pub_date']
