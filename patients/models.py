from django.db import models

# Create your models here.
class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    national_id = models.CharField(max_length=20, unique=True)
    insurance_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.full_name
    
    