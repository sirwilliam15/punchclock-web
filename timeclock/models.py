from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

class Timecard(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField()
    status = models.BooleanField()