from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50,unique = True)
    phone = models.CharField(max_length=15)
    salary = models.FloatField()
    
    def __str__(self):
        return self.name