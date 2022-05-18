from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    customer_num = models.IntegerField()
    reservation_date = models.CharField(max_length=10)
    reservation_time = models.CharField(max_length=10)
    
    